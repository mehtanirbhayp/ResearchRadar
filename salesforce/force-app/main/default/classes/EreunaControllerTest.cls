@isTest
private class EreunaControllerTest {

    @testSetup
    static void setup() {
        EreunaDataService.seedResearchData();
    }

    @isTest
    static void testGetRecentMaps() {
        Test.startTest();
        List<Research_Map__c> mapsAll = EreunaController.getRecentMaps('All');
        List<Research_Map__c> mapsCloud = EreunaController.getRecentMaps('Cloud Computing');
        Test.stopTest();

        System.assertNotEquals(0, mapsAll.size(), 'Should return seeded maps');
        System.assertNotEquals(0, mapsCloud.size(), 'Should return seeded cloud maps');
    }

    @isTest
    static void testGetMapDetailsAndRelations() {
        Research_Map__c rm = [SELECT Id FROM Research_Map__c LIMIT 1];

        Test.startTest();
        Research_Map__c details = EreunaController.getMapDetails(rm.Id);
        List<Map_Paper_Link__c> papers = EreunaController.getMapPapers(rm.Id);
        List<Research_Finding__c> findings = EreunaController.getMapFindings(rm.Id);
        List<Research_Conflict__c> conflicts = EreunaController.getMapConflicts(rm.Id);
        List<Research_Gap__c> gaps = EreunaController.getMapGaps(rm.Id);
        EreunaController.GraphDataWrapper graph = EreunaController.getCitationNetwork(rm.Id);
        Test.stopTest();

        System.assertNotEquals(null, details, 'Map details should not be null');
        System.assertNotEquals(0, papers.size(), 'Map should have linked papers');
        System.assertNotEquals(null, graph, 'Graph data wrapper should not be null');
        System.assertNotEquals(0, graph.nodes.size(), 'Graph should have paper nodes');
    }

    @isTest
    static void testCreateOrSynthesizeMap() {
        Test.startTest();
        Research_Map__c createdMap = EreunaController.createOrSynthesizeMap('Edge Computing Orchestration', 'Cloud Computing');
        Test.stopTest();

        System.assertNotEquals(null, createdMap, 'Created map should exist');
        System.assertEquals('Synthesized', createdMap.Status__c, 'Status should be Synthesized');
    }

    @isTest
    static void testUpdateGapStatus() {
        Research_Gap__c gap = [SELECT Id, Status__c FROM Research_Gap__c LIMIT 1];

        Test.startTest();
        String result = EreunaController.updateGapStatus(gap.Id, 'In Review');
        Test.stopTest();

        System.assertEquals('SUCCESS', result, 'Update should succeed');
        Research_Gap__c updated = [SELECT Status__c FROM Research_Gap__c WHERE Id = :gap.Id];
        System.assertEquals('In Review', updated.Status__c, 'Status should be In Review');
    }

    @isTest
    static void testInitializeSampleData() {
        Test.startTest();
        Map<String, Object> res = EreunaController.initializeSampleData();
        Test.stopTest();

        System.assertEquals('SUCCESS', (String)res.get('status'), 'Initialization should return SUCCESS');
    }
}
