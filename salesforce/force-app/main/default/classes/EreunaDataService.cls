/**
 * @description Service to seed and manage realistic academic literature data for Cloud Computing research maps.
 * Aligned with BMEE355E Cloud Computing curriculum.
 */
public with sharing class EreunaDataService {
    
    /**
     * Seeds comprehensive research maps, papers, findings, benchmarks, conflicts, and gaps.
     * Can be invoked from LWC or Anonymous Apex.
     */
    public static Map<String, Object> seedResearchData() {
        Map<String, Object> result = new Map<String, Object>();
        
        // 1. Papers
        List<Research_Paper__c> papersToInsert = new List<Research_Paper__c>();
        
        Research_Paper__c p1 = new Research_Paper__c(
            Name = 'Serverless Cold-Start Analysis in Multi-Tenant Clouds',
            Title__c = 'Serverless Cold-Start Analysis in Multi-Tenant Clouds',
            Authors__c = 'Nirbhay Mehta, Sarah Jenkins, David K. Miller',
            DOI__c = '10.1145/3419111.3421285',
            Publication_Year__c = 2023,
            Venue__c = 'ACM Symposium on Cloud Computing (SoCC)',
            Abstract__c = 'Serverless Function-as-a-Service (FaaS) offers fine-grained elasticity but suffers from container initialization latency (cold-starts). We analyze memory-aware pre-warming and snapshot restoration across 10,000 invocations.',
            Citation_Count__c = 142,
            Open_Access_URL__c = 'https://arxiv.org/abs/2301.04182',
            PDF_URL__c = 'https://arxiv.org/pdf/2301.04182.pdf',
            Primary_Discipline__c = 'Cloud Computing'
        );
        papersToInsert.add(p1);

        Research_Paper__c p2 = new Research_Paper__c(
            Name = 'Adaptive Resource Scheduling for Kubernetes Clusters',
            Title__c = 'Adaptive Resource Scheduling for Kubernetes Clusters',
            Authors__c = 'Elena Rostova, Amit Patel, Marcus Vance',
            DOI__c = '10.1109/TCC.2024.3129841',
            Publication_Year__c = 2024,
            Venue__c = 'IEEE Transactions on Cloud Computing',
            Abstract__c = 'Dynamic pod placement algorithms minimizing resource fragmentation while maintaining SLA compliance for batch and streaming workloads in heterogeneous cloud environments.',
            Citation_Count__c = 89,
            Open_Access_URL__c = 'https://arxiv.org/abs/2402.09112',
            PDF_URL__c = 'https://arxiv.org/pdf/2402.09112.pdf',
            Primary_Discipline__c = 'Cloud Computing'
        );
        papersToInsert.add(p2);

        Research_Paper__c p3 = new Research_Paper__c(
            Name = 'Zero-Trust Architecture in Hybrid Cloud Microservices',
            Title__c = 'Zero-Trust Architecture in Hybrid Cloud Microservices',
            Authors__c = 'Tariq Al-Mansoor, Li Wei, Brenda Cooper',
            DOI__c = '10.1145/3548606.3560610',
            Publication_Year__c = 2023,
            Venue__c = 'ACM Conference on Computer and Communications Security (CCS)',
            Abstract__c = 'Evaluates mutual TLS (mTLS) overhead with eBPF service meshes in hybrid-cloud deployments, demonstrating cryptographic identity verification with sub-millisecond p99 latency.',
            Citation_Count__c = 210,
            Open_Access_URL__c = 'https://arxiv.org/abs/2305.10984',
            PDF_URL__c = 'https://arxiv.org/pdf/2305.10984.pdf',
            Primary_Discipline__c = 'Cloud Computing'
        );
        papersToInsert.add(p3);

        Research_Paper__c p4 = new Research_Paper__c(
            Name = 'Carbon-Aware Workload Orchestration across Global Cloud Regions',
            Title__c = 'Carbon-Aware Workload Orchestration across Global Cloud Regions',
            Authors__c = 'Kavita Sundaram, Lucas Dupont, Hans Gruber',
            DOI__c = '10.1145/3639478.3640021',
            Publication_Year__c = 2025,
            Venue__c = 'USENIX Conference on Operational Systems & Cloud',
            Abstract__c = 'Shifting elastic batch processing jobs across geographic cloud datacenters according to real-time grid carbon intensity reduced greenhouse emissions by 34% with under 5% SLA impact.',
            Citation_Count__c = 34,
            Open_Access_URL__c = 'https://arxiv.org/abs/2501.07721',
            PDF_URL__c = 'https://arxiv.org/pdf/2501.07721.pdf',
            Primary_Discipline__c = 'Cloud Computing'
        );
        papersToInsert.add(p4);

        upsert papersToInsert DOI__c;

        // 2. Extracted Metrics for Papers
        List<Extracted_Metric__c> metrics = new List<Extracted_Metric__c>();
        metrics.add(new Extracted_Metric__c(
            Research_Paper__c = p1.Id,
            Metric_Name__c = 'Cold Start P99 Latency',
            Metric_Value__c = 184.2,
            Unit__c = 'ms',
            Benchmark_Dataset__c = 'AWS Lambda Microbenchmarks'
        ));
        metrics.add(new Extracted_Metric__c(
            Research_Paper__c = p1.Id,
            Metric_Name__c = 'Memory Footprint Reduction',
            Metric_Value__c = 42.5,
            Unit__c = '%',
            Benchmark_Dataset__c = 'Firecracker MicroVM Bench'
        ));
        metrics.add(new Extracted_Metric__c(
            Research_Paper__c = p2.Id,
            Metric_Name__c = 'Cluster CPU Utilization',
            Metric_Value__c = 78.4,
            Unit__c = '%',
            Benchmark_Dataset__c = 'Google Cluster Traces 2019'
        ));
        metrics.add(new Extracted_Metric__c(
            Research_Paper__c = p3.Id,
            Metric_Name__c = 'Network Latency Overhead',
            Metric_Value__c = 1.15,
            Unit__c = 'ms',
            Benchmark_Dataset__c = 'Cilium eBPF Mesh Suite'
        ));
        metrics.add(new Extracted_Metric__c(
            Research_Paper__c = p4.Id,
            Metric_Name__c = 'Carbon Emission Abatement',
            Metric_Value__c = 34.0,
            Unit__c = '%',
            Benchmark_Dataset__c = 'Electricity Maps Grid Trace'
        ));
        insert metrics;

        // 3. Research Maps
        Research_Map__c mapCloud = new Research_Map__c(
            Topic__c = 'Serverless Elasticity and Cold-Start Mitigation in Multi-Cloud Systems',
            Status__c = 'Synthesized',
            Target_Discipline__c = 'Cloud Computing',
            Synthesis_Summary__c = 'Modern cloud systems balance cold-start latency against idle compute cost. Current consensus favors microVM snapshots (Firecracker) combined with predictive pre-warming over passive idle keep-alives. Disagreements persist regarding memory bloat in high-concurrency environments.'
        );
        insert mapCloud;

        Research_Map__c mapSec = new Research_Map__c(
            Topic__c = 'Zero-Trust Security & Carbon-Aware Scheduling in Distributed Cloud Platforms',
            Status__c = 'Synthesized',
            Target_Discipline__c = 'Cloud Computing',
            Synthesis_Summary__c = 'Microservice architectures are converging towards eBPF-based cryptographic identities. Simultaneously, geo-distributed clusters are utilizing spot-instance migrations to track real-time low-carbon energy availability across global zones.'
        );
        insert mapSec;

        // 4. Map-Paper Links
        List<Map_Paper_Link__c> links = new List<Map_Paper_Link__c>();
        links.add(new Map_Paper_Link__c(Research_Map__c = mapCloud.Id, Research_Paper__c = p1.Id, Relevance_Score__c = 96.5, Inclusion_Rationale__c = 'Primary benchmark for microVM snapshot restoration latency'));
        links.add(new Map_Paper_Link__c(Research_Map__c = mapCloud.Id, Research_Paper__c = p2.Id, Relevance_Score__c = 88.0, Inclusion_Rationale__c = 'Provides container orchestration and auto-scaling baseline'));
        links.add(new Map_Paper_Link__c(Research_Map__c = mapSec.Id, Research_Paper__c = p3.Id, Relevance_Score__c = 98.0, Inclusion_Rationale__c = 'Foundational study on eBPF mTLS performance in hybrid clouds'));
        links.add(new Map_Paper_Link__c(Research_Map__c = mapSec.Id, Research_Paper__c = p4.Id, Relevance_Score__c = 91.5, Inclusion_Rationale__c = 'Examines multi-region workload shifting with green SLA guarantees'));
        insert links;

        // 5. Research Findings
        List<Research_Finding__c> findings = new List<Research_Finding__c>();
        findings.add(new Research_Finding__c(
            Research_Map__c = mapCloud.Id,
            Research_Paper__c = p1.Id,
            Claim_Summary__c = 'Memory pre-warming reduces 99th percentile cold start by 68%.',
            Exact_Quote__c = 'By maintaining an in-memory page tree of common runtime libraries, container initialization dropped from 580ms to 184ms across ten thousand test trials.',
            Page_Number__c = 4,
            Section_Name__c = '4.2 Evaluation of Warm-Start Page Sharing',
            Verification_Status__c = 'Verified',
            Confidence_Score__c = 99.4
        ));
        findings.add(new Research_Finding__c(
            Research_Map__c = mapCloud.Id,
            Research_Paper__c = p2.Id,
            Claim_Summary__c = 'Dynamic bin-packing lowers cluster node count by 23% without breaching SLAs.',
            Exact_Quote__c = 'Our scheduler packed bursty workloads with 23% fewer compute instances than default Kubernetes kube-scheduler.',
            Page_Number__c = 7,
            Section_Name__c = '5. Experimental Results',
            Verification_Status__c = 'Verified',
            Confidence_Score__c = 94.8
        ));
        findings.add(new Research_Finding__c(
            Research_Map__c = mapSec.Id,
            Research_Paper__c = p3.Id,
            Claim_Summary__c = 'eBPF data plane bypasses socket buffers, reducing sidecar proxy latency to 1.15ms.',
            Exact_Quote__c = 'Kernel-level sockops redirection eliminates user-space context switches for service mesh proxies, achieving p99 response times of 1.15ms.',
            Page_Number__c = 6,
            Section_Name__c = '6. Sidecar-Free Service Mesh Benchmarks',
            Verification_Status__c = 'Verified',
            Confidence_Score__c = 98.2
        ));
        insert findings;

        // 6. Conflicts
        List<Research_Conflict__c> conflicts = new List<Research_Conflict__c>();
        conflicts.add(new Research_Conflict__c(
            Research_Map__c = mapCloud.Id,
            Paper_A__c = p1.Id,
            Paper_B__c = p2.Id,
            Disagreement_Area__c = 'Memory Overcommit Feasibility in Serverless vs Stateful Pods',
            Conflict_Description__c = 'Paper 1 argues that memory snapshotting allows aggressive host memory overcommit up to 2.5x without throttling, whereas Paper 2 demonstrates that dynamic scheduling causes severe page-fault cascades when overcommit exceeds 1.3x under bursty traffic.',
            Severity__c = 'Moderate'
        ));
        insert conflicts;

        // 7. Gaps
        List<Research_Gap__c> gaps = new List<Research_Gap__c>();
        gaps.add(new Research_Gap__c(
            Research_Map__c = mapCloud.Id,
            Problem_Statement__c = 'Lack of hardware-assisted memory snapshotting across heterogeneous ARM and x86 cloud nodes.',
            Proposed_Experiment__c = 'Benchmark cross-architecture snapshot migration using unified memory pages between Graviton3 and AMD EPYC servers under synthetic financial micro-benchmarks.',
            Priority__c = 'High',
            Estimated_Complexity__c = 'High',
            Status__c = 'Experiment Drafted'
        ));
        gaps.add(new Research_Gap__c(
            Research_Map__c = mapSec.Id,
            Problem_Statement__c = 'Carbon-aware migration can induce cryptographic re-handshake storms across zero-trust cloud boundaries.',
            Proposed_Experiment__c = 'Deploy an automated state-transfer session cache that pre-propagates mutual TLS tickets to target green data centers 30 seconds prior to live container migration.',
            Priority__c = 'High',
            Estimated_Complexity__c = 'Medium',
            Status__c = 'Identified'
        ));
        insert gaps;

        result.put('status', 'SUCCESS');
        result.put('papersCount', papersToInsert.size());
        result.put('mapsCount', 2);
        result.put('findingsCount', findings.size());
        result.put('gapsCount', gaps.size());
        return result;
    }
}
