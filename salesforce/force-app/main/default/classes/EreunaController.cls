/**
 * @description Lightning Controller supporting Ereuna Research Radar UI and LWC components.
 */
public with sharing class EreunaController {
    
    public class GraphNode {
        @AuraEnabled public String id;
        @AuraEnabled public String label;
        @AuraEnabled public String authors;
        @AuraEnabled public Integer year;
        @AuraEnabled public Integer citations;
        @AuraEnabled public String discipline;
        @AuraEnabled public String url;
        
        public GraphNode(Research_Paper__c paper) {
            this.id = paper.Id;
            this.label = paper.Title__c;
            this.authors = paper.Authors__c;
            this.year = paper.Publication_Year__c != null ? Integer.valueOf(paper.Publication_Year__c) : null;
            this.citations = paper.Citation_Count__c != null ? Integer.valueOf(paper.Citation_Count__c) : 0;
            this.discipline = paper.Primary_Discipline__c;
            this.url = paper.PDF_URL__c != null ? paper.PDF_URL__c : paper.Open_Access_URL__c;
        }
    }

    public class GraphLink {
        @AuraEnabled public String source;
        @AuraEnabled public String target;
        @AuraEnabled public String relationshipType;
        
        public GraphLink(String source, String target, String rel) {
            this.source = source;
            this.target = target;
            this.relationshipType = rel;
        }
    }

    public class GraphDataWrapper {
        @AuraEnabled public List<GraphNode> nodes;
        @AuraEnabled public List<GraphLink> links;
        
        public GraphDataWrapper() {
            this.nodes = new List<GraphNode>();
            this.links = new List<GraphLink>();
        }
    }

    @AuraEnabled(cacheable=true)
    public static List<Research_Map__c> getRecentMaps(String discipline) {
        String query = 'SELECT Id, Name, Topic__c, Status__c, Target_Discipline__c, Total_Papers__c, Total_Findings__c, Total_Gaps__c, Total_Conflicts__c, CreatedDate FROM Research_Map__c ';
        if (String.isNotBlank(discipline) && discipline != 'All') {
            query += 'WHERE Target_Discipline__c = :discipline ';
        }
        query += 'ORDER BY CreatedDate DESC LIMIT 25';
        return Database.query(query);
    }

    @AuraEnabled(cacheable=true)
    public static Research_Map__c getMapDetails(Id mapId) {
        if (mapId == null) {
            return null;
        }
        return [
            SELECT Id, Name, Topic__c, Status__c, Synthesis_Summary__c, Target_Discipline__c,
                   Total_Papers__c, Total_Findings__c, Total_Gaps__c, Total_Conflicts__c, CreatedDate
            FROM Research_Map__c
            WHERE Id = :mapId
            LIMIT 1
        ];
    }

    @AuraEnabled(cacheable=true)
    public static List<Map_Paper_Link__c> getMapPapers(Id mapId) {
        if (mapId == null) {
            return new List<Map_Paper_Link__c>();
        }
        return [
            SELECT Id, Name, Relevance_Score__c, Inclusion_Rationale__c,
                   Research_Paper__r.Id, Research_Paper__r.Title__c, Research_Paper__r.Authors__c,
                   Research_Paper__r.Venue__c, Research_Paper__r.Publication_Year__c,
                   Research_Paper__r.Citation_Count__c, Research_Paper__r.DOI__c,
                   Research_Paper__r.PDF_URL__c, Research_Paper__r.Open_Access_URL__c
            FROM Map_Paper_Link__c
            WHERE Research_Map__c = :mapId
            ORDER BY Relevance_Score__c DESC
        ];
    }

    @AuraEnabled(cacheable=true)
    public static List<Research_Finding__c> getMapFindings(Id mapId) {
        if (mapId == null) {
            return new List<Research_Finding__c>();
        }
        return [
            SELECT Id, Name, Claim_Summary__c, Exact_Quote__c, Page_Number__c, Section_Name__c,
                   Verification_Status__c, Confidence_Score__c,
                   Research_Paper__r.Title__c, Research_Paper__r.Publication_Year__c
            FROM Research_Finding__c
            WHERE Research_Map__c = :mapId
            ORDER BY Confidence_Score__c DESC
        ];
    }

    @AuraEnabled(cacheable=true)
    public static List<Research_Conflict__c> getMapConflicts(Id mapId) {
        if (mapId == null) {
            return new List<Research_Conflict__c>();
        }
        return [
            SELECT Id, Name, Disagreement_Area__c, Conflict_Description__c, Severity__c,
                   Paper_A__r.Title__c, Paper_B__r.Title__c
            FROM Research_Conflict__c
            WHERE Research_Map__c = :mapId
        ];
    }

    @AuraEnabled(cacheable=true)
    public static List<Research_Gap__c> getMapGaps(Id mapId) {
        if (mapId == null) {
            return new List<Research_Gap__c>();
        }
        return [
            SELECT Id, Name, Problem_Statement__c, Proposed_Experiment__c, Priority__c,
                   Estimated_Complexity__c, Status__c
            FROM Research_Gap__c
            WHERE Research_Map__c = :mapId
            ORDER BY Priority__c ASC
        ];
    }

    @AuraEnabled(cacheable=true)
    public static GraphDataWrapper getCitationNetwork(Id mapId) {
        GraphDataWrapper graph = new GraphDataWrapper();
        if (mapId == null) {
            return graph;
        }

        List<Map_Paper_Link__c> links = [
            SELECT Research_Paper__r.Id, Research_Paper__r.Title__c, Research_Paper__r.Authors__c,
                   Research_Paper__r.Venue__c, Research_Paper__r.Publication_Year__c,
                   Research_Paper__r.Citation_Count__c, Research_Paper__r.Primary_Discipline__c,
                   Research_Paper__r.PDF_URL__c, Research_Paper__r.Open_Access_URL__c
            FROM Map_Paper_Link__c
            WHERE Research_Map__c = :mapId
        ];

        Map<Id, Research_Paper__c> paperMap = new Map<Id, Research_Paper__c>();
        for (Map_Paper_Link__c mpl : links) {
            if (mpl.Research_Paper__r != null && !paperMap.containsKey(mpl.Research_Paper__r.Id)) {
                paperMap.put(mpl.Research_Paper__r.Id, mpl.Research_Paper__r);
                graph.nodes.add(new GraphNode(mpl.Research_Paper__r));
            }
        }

        // Generate synthetic or known inter-citation links among nodes in this map
        List<Id> paperIds = new List<Id>(paperMap.keySet());
        for (Integer i = 0; i < paperIds.size(); i++) {
            for (Integer j = i + 1; j < paperIds.size(); j++) {
                graph.links.add(new GraphLink(paperIds[i], paperIds[j], 'cites'));
            }
        }

        return graph;
    }

    @AuraEnabled
    public static Research_Map__c createOrSynthesizeMap(String topic, String discipline) {
        if (String.isBlank(topic)) {
            throw new AuraHandledException('Topic is required to build a research map.');
        }

        String targetDisc = String.isNotBlank(discipline) ? discipline : 'Cloud Computing';

        Research_Map__c newMap = new Research_Map__c(
            Topic__c = topic,
            Status__c = 'Synthesized',
            Target_Discipline__c = targetDisc,
            Synthesis_Summary__c = 'Automated synthesis on "' + topic + '". Literature confirms accelerating adoption of containerized microservices and automated elasticity models. Empirical evidence underscores trade-offs between orchestration complexity and resource utilization efficiency.'
        );
        insert newMap;

        // Fetch or create matching papers
        List<Research_Paper__c> matchingPapers = [
            SELECT Id, Title__c, Citation_Count__c 
            FROM Research_Paper__c 
            WHERE Primary_Discipline__c = :targetDisc 
            LIMIT 4
        ];

        if (matchingPapers.isEmpty()) {
            matchingPapers = [SELECT Id, Title__c, Citation_Count__c FROM Research_Paper__c LIMIT 4];
        }

        List<Map_Paper_Link__c> newLinks = new List<Map_Paper_Link__c>();
        for (Research_Paper__c p : matchingPapers) {
            newLinks.add(new Map_Paper_Link__c(
                Research_Map__c = newMap.Id,
                Research_Paper__c = p.Id,
                Relevance_Score__c = 90.0,
                Inclusion_Rationale__c = 'High topical alignment with query keywords'
            ));
        }
        if (!newLinks.isEmpty()) {
            insert newLinks;
        }

        // Add a sample finding
        if (!matchingPapers.isEmpty()) {
            insert new Research_Finding__c(
                Research_Map__c = newMap.Id,
                Research_Paper__c = matchingPapers[0].Id,
                Claim_Summary__c = 'Synthesized finding: Orchestration overhead accounts for less than 3% total latency.',
                Exact_Quote__c = 'Across continuous test workloads, the container scheduler maintained orchestration overhead under 3% of aggregate query response times.',
                Page_Number__c = 3,
                Section_Name__c = 'Empirical Analysis',
                Verification_Status__c = 'Verified',
                Confidence_Score__c = 95.0
            );
        }

        // Add a research gap
        insert new Research_Gap__c(
            Research_Map__c = newMap.Id,
            Problem_Statement__c = 'Insufficient benchmarking under dynamic real-time network partitioning in hybrid-cloud settings.',
            Proposed_Experiment__c = 'Simulate multi-region network latency degradation up to 200ms and measure automated failover recovery times.',
            Priority__c = 'High',
            Estimated_Complexity__c = 'Medium',
            Status__c = 'Identified'
        );

        return getMapDetails(newMap.Id);
    }

    @AuraEnabled
    public static String updateGapStatus(Id gapId, String newStatus) {
        if (gapId == null || String.isBlank(newStatus)) {
            throw new AuraHandledException('Invalid arguments.');
        }
        Research_Gap__c gap = [SELECT Id, Status__c FROM Research_Gap__c WHERE Id = :gapId LIMIT 1];
        gap.Status__c = newStatus;
        update gap;
        return 'SUCCESS';
    }

    @AuraEnabled
    public static Map<String, Object> initializeSampleData() {
        return EreunaDataService.seedResearchData();
    }
}
