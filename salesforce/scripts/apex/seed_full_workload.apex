
// Execute Full Comprehensive Dataset Seeding for Research Radar
System.debug('Starting Comprehensive Research Data Seeding...');

// ---------------------------------------------------------
// 1. RESEARCH PAPERS (24 realistic peer-reviewed papers)
// ---------------------------------------------------------
List<Research_Paper__c> papers = new List<Research_Paper__c>();

// P1
papers.add(new Research_Paper__c(
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
));

// P2
papers.add(new Research_Paper__c(
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
));

// P3
papers.add(new Research_Paper__c(
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
));

// P4
papers.add(new Research_Paper__c(
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
));

// P5
papers.add(new Research_Paper__c(
    Name = 'Firecracker: Lightweight Virtualization for Serverless Workloads',
    Title__c = 'Firecracker: Lightweight Virtualization for Serverless Workloads',
    Authors__c = 'Alexandru Agache, Marc Brooker, Andreea Florescu, Alexandra Iordache',
    DOI__c = '10.5555/3342195.3387542',
    Publication_Year__c = 2022,
    Venue__c = 'USENIX Symposium on Networked Systems Design and Implementation (NSDI)',
    Abstract__c = 'Introduces microVMs based on Linux KVM providing strong hardware isolation with sub-5ms boot times and 5MB per-instance memory footprint, replacing conventional full virtualization in cloud multi-tenancy.',
    Citation_Count__c = 485,
    Open_Access_URL__c = 'https://www.usenix.org/conference/nsdi20/presentation/agache',
    PDF_URL__c = 'https://www.usenix.org/system/files/nsdi20-paper-agache.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P6
papers.add(new Research_Paper__c(
    Name = 'Sidecar-Free Service Meshes: High-Performance Networking with eBPF',
    Title__c = 'Sidecar-Free Service Meshes: High-Performance Networking with eBPF',
    Authors__c = 'Thomas Graf, Daniel Borkmann, Alexei Starovoitov',
    DOI__c = '10.1145/3544216.3544230',
    Publication_Year__c = 2023,
    Venue__c = 'ACM SIGCOMM Workshop on eBPF and Kernel Extensions',
    Abstract__c = 'Replaces per-pod Envoy sidecar proxies with host-level eBPF sockops programs, cutting CPU utilization in half and reducing tail latency in high-throughput cloud microservices.',
    Citation_Count__c = 176,
    Open_Access_URL__c = 'https://arxiv.org/abs/2303.02981',
    PDF_URL__c = 'https://arxiv.org/pdf/2303.02981.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P7
papers.add(new Research_Paper__c(
    Name = 'Borg: The Cluster Management System at Scale',
    Title__c = 'Large-scale Cluster Management at Google with Borg',
    Authors__c = 'Abhishek Verma, Luis Pedrosa, Madhukar Korupolu, David Oppenheimer',
    DOI__c = '10.1145/2741948.2741964',
    Publication_Year__c = 2021,
    Venue__c = 'ACM European Conference on Computer Systems (EuroSys)',
    Abstract__c = 'Describes Borg, Google cluster manager that runs hundreds of thousands of jobs from many thousands of different applications across tens of thousands of machines with priority-based preemption.',
    Citation_Count__c = 430,
    Open_Access_URL__c = 'https://research.google/pubs/pub43438/',
    PDF_URL__c = 'https://storage.googleapis.com/gweb-research2023-media/pubfile/43438.pdf',
    Primary_Discipline__c = 'Distributed Systems'
));

// P8
papers.add(new Research_Paper__c(
    Name = 'Carbon-Aware Computing: Measuring and Mitigating Data Center Emissions',
    Title__c = 'Carbon-Aware Computing: Measuring and Mitigating Data Center Emissions',
    Authors__c = 'Ana Radovanovic, Ross Koningstein, Ian Schneider, Bokan Chen',
    DOI__c = '10.1145/3575693.3575701',
    Publication_Year__c = 2023,
    Venue__c = 'Communications of the ACM (CACM)',
    Abstract__c = 'A global carbon-intelligent computing platform that shifts non-urgent compute tasks in time and location to track variable solar and wind energy production across worldwide datacenters.',
    Citation_Count__c = 194,
    Open_Access_URL__c = 'https://dl.acm.org/doi/10.1145/3575693.3575701',
    PDF_URL__c = 'https://arxiv.org/pdf/2106.11750.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P9
papers.add(new Research_Paper__c(
    Name = 'WasmEdge: Serverless WebAssembly Runtime for Edge-Cloud Synergy',
    Title__c = 'WasmEdge: Serverless WebAssembly Runtime for Edge-Cloud Synergy',
    Authors__c = 'Michael Yuan, Hung-Ying Tai, Shen-Ta Hsieh',
    DOI__c = '10.1109/IC2E52221.2023.00018',
    Publication_Year__c = 2023,
    Venue__c = 'IEEE International Conference on Cloud Engineering (IC2E)',
    Abstract__c = 'Demonstrates bytecode sandboxing via WebAssembly runtimes that start in under 50 microseconds, reducing cold-start latency by two orders of magnitude compared to OCI container runtimes on resource-constrained edge gateways.',
    Citation_Count__c = 82,
    Open_Access_URL__c = 'https://arxiv.org/abs/2304.14882',
    PDF_URL__c = 'https://arxiv.org/pdf/2304.14882.pdf',
    Primary_Discipline__c = 'Distributed Systems'
));

// P10
papers.add(new Research_Paper__c(
    Name = 'Confidential Virtual Machines: Performance and Attack Surfaces',
    Title__c = 'Confidential Virtual Machines: Performance and Attack Surfaces',
    Authors__c = 'Dmitry Parno, Mona Gupta, Jason Gross, Bryan Parno',
    DOI__c = '10.1109/SP46215.2024.1053142',
    Publication_Year__c = 2024,
    Venue__c = 'IEEE Symposium on Security and Privacy (S&P)',
    Abstract__c = 'Comprehensive benchmark of AMD SEV-SNP and Intel TDX in public clouds. Demonstrates full memory encryption with 6.2% average compute degradation, though nested page faults incur severe I/O penalties for databases.',
    Citation_Count__c = 112,
    Open_Access_URL__c = 'https://arxiv.org/abs/2401.08942',
    PDF_URL__c = 'https://arxiv.org/pdf/2401.08942.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P11
papers.add(new Research_Paper__c(
    Name = 'SpotArbitrage: Predictive Multi-Cloud Spot Instance Trading',
    Title__c = 'SpotArbitrage: Predictive Multi-Cloud Spot Instance Trading',
    Authors__c = 'Ravi Shankar, Chen Zhang, Priya Balasubramanian',
    DOI__c = '10.1145/3627703.3629581',
    Publication_Year__c = 2024,
    Venue__c = 'ACM Symposium on Cloud Computing (SoCC)',
    Abstract__c = 'Reinforcement learning model that forecasts spot market preemption probabilities across AWS, Azure, and Google Cloud, executing preemptive workload migration with zero lost progress and 58% cost savings.',
    Citation_Count__c = 67,
    Open_Access_URL__c = 'https://arxiv.org/abs/2403.01189',
    PDF_URL__c = 'https://arxiv.org/pdf/2403.01189.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P12
papers.add(new Research_Paper__c(
    Name = 'Disaggregated Memory Architecture with CXL for Cloud Datacenters',
    Title__c = 'Disaggregated Memory Architecture with CXL for Cloud Datacenters',
    Authors__c = 'Huaicheng Li, Daniel S. Berger, Lisa Hsu, Dan Tsafrir',
    DOI__c = '10.1145/3563766.3564082',
    Publication_Year__c = 2023,
    Venue__c = 'ACM International Conference on Architectural Support for Programming Languages (ASPLOS)',
    Abstract__c = 'Evaluates Compute Express Link (CXL) pooled memory in production cloud environments. Demonstrates a 14% overall reduction in unallocated DRAM across hypervisors with acceptable cache coherency latency.',
    Citation_Count__c = 153,
    Open_Access_URL__c = 'https://arxiv.org/abs/2306.00223',
    PDF_URL__c = 'https://arxiv.org/pdf/2306.00223.pdf',
    Primary_Discipline__c = 'Distributed Systems'
));

// P13
papers.add(new Research_Paper__c(
    Name = 'Faasm: Lightweight Isolation for Efficient Stateful Serverless Computing',
    Title__c = 'Faasm: Lightweight Isolation for Efficient Stateful Serverless Computing',
    Authors__c = 'Simon Shillaker, Peter Pietzuch',
    DOI__c = '10.5555/3489146.3489178',
    Publication_Year__c = 2022,
    Venue__c = 'USENIX Annual Technical Conference (ATC)',
    Abstract__c = 'Introduces Faasm, a serverless runtime that isolates tenant functions within shared address spaces using WebAssembly, enabling zero-copy shared memory communication across concurrent function invocations.',
    Citation_Count__c = 224,
    Open_Access_URL__c = 'https://www.usenix.org/conference/atc20/presentation/shillaker',
    PDF_URL__c = 'https://www.usenix.org/system/files/atc20-shillaker.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P14
papers.add(new Research_Paper__c(
    Name = 'Cilium: BPF-Powered Networking, Observability, and Security for Kubernetes',
    Title__c = 'Cilium: BPF-Powered Networking, Observability, and Security for Kubernetes',
    Authors__c = 'Joe Stringer, Martynas Pumputis, Thomas Graf',
    DOI__c = '10.1145/3472883.3473180',
    Publication_Year__c = 2022,
    Venue__c = 'ACM SIGCOMM eBPF Workshop',
    Abstract__c = 'Documents the deployment of Cilium across hundreds of Kubernetes clusters, proving that kernel-level BPF programs enforce Layer 3-7 security policies at wire speed without iptables lock contention.',
    Citation_Count__c = 165,
    Open_Access_URL__c = 'https://ebpf.io/summit-2022/',
    PDF_URL__c = 'https://arxiv.org/pdf/2208.11200.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P15
papers.add(new Research_Paper__c(
    Name = 'Firmament: Fast, Centralized Cluster Scheduling with Network Flow',
    Title__c = 'Firmament: Fast, Centralized Cluster Scheduling with Network Flow',
    Authors__c = 'Ionel Gog, Malte Schwarzkopf, Adam Gleave, Robert N. M. Watson',
    DOI__c = '10.5555/3026877.3026886',
    Publication_Year__c = 2021,
    Venue__c = 'USENIX Symposium on Operating Systems Design and Implementation (OSDI)',
    Abstract__c = 'Solves the cluster scheduling problem using minimum-cost max-flow optimization over a dynamic graph, making optimal placement decisions for 10,000 tasks in under 15 milliseconds.',
    Citation_Count__c = 310,
    Open_Access_URL__c = 'https://www.usenix.org/conference/osdi16/technical-sessions/presentation/gog',
    PDF_URL__c = 'https://www.usenix.org/system/files/osdi16-gog.pdf',
    Primary_Discipline__c = 'Distributed Systems'
));

// P16
papers.add(new Research_Paper__c(
    Name = 'Ecological Footprint of AI Cloud Training: Measurement & Mitigation',
    Title__c = 'Ecological Footprint of Large Model Training in Public Cloud Infrastructure',
    Authors__c = 'David Patterson, Joseph Gonzalez, Urs Holzle, Quoc Le',
    DOI__c = '10.1145/3488659.3493776',
    Publication_Year__c = 2022,
    Venue__c = 'IEEE Computer Magazine',
    Abstract__c = 'Analyzes real-world energy and carbon emissions for training GPT-3 and other foundation models. Shows that choosing green datacenter locations and modern ML accelerators reduces carbon impact by 100x.',
    Citation_Count__c = 340,
    Open_Access_URL__c = 'https://arxiv.org/abs/2104.10350',
    PDF_URL__c = 'https://arxiv.org/pdf/2104.10350.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P17
papers.add(new Research_Paper__c(
    Name = 'Fogflow: City-Scale Edge Intelligence and Dynamic Topology Orchestration',
    Title__c = 'Fogflow: City-Scale Edge Intelligence and Dynamic Topology Orchestration',
    Authors__c = 'Bin Cheng, Jonathan Furst, Gurkan Solmaz, Ernö Kovacs',
    DOI__c = '10.1109/MWC.2021.9360871',
    Publication_Year__c = 2022,
    Venue__c = 'IEEE Wireless Communications',
    Abstract__c = 'A standardized edge orchestration framework supporting dynamic data processing workflows over heterogeneous roadside edge nodes and centralized cloud infrastructures for smart cities.',
    Citation_Count__c = 95,
    Open_Access_URL__c = 'https://arxiv.org/abs/2103.04561',
    PDF_URL__c = 'https://arxiv.org/pdf/2103.04561.pdf',
    Primary_Discipline__c = 'Distributed Systems'
));

// P18
papers.add(new Research_Paper__c(
    Name = 'SCONE: Secure Linux Containers with Intel SGX',
    Title__c = 'SCONE: Secure Linux Containers with Intel SGX',
    Authors__c = 'Sergei Arnautov, Bohdan Trach, Franz Gregor, Thomas Knauth',
    DOI__c = '10.5555/3026877.3026922',
    Publication_Year__c = 2021,
    Venue__c = 'USENIX Symposium on Operating Systems Design and Implementation (OSDI)',
    Abstract__c = 'Enables unmodified POSIX applications to execute securely inside Intel SGX enclaves, protecting data from untrusted root users and compromised cloud provider operating systems.',
    Citation_Count__c = 415,
    Open_Access_URL__c = 'https://www.usenix.org/conference/osdi16/technical-sessions/presentation/arnautov',
    PDF_URL__c = 'https://www.usenix.org/system/files/osdi16-arnautov.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P19
papers.add(new Research_Paper__c(
    Name = 'FinOps for Kubernetes: Cost Attribution and Autoscaling in Multi-Tenant Clusters',
    Title__c = 'FinOps for Kubernetes: Cost Attribution and Autoscaling in Multi-Tenant Clusters',
    Authors__c = 'Webb Horn, Ajay Kulkarni, Nicole Forsgren',
    DOI__c = '10.1145/3542929.3563478',
    Publication_Year__c = 2023,
    Venue__c = 'ACM Cloud FinOps Symposium',
    Abstract__c = 'Presents granular container-level cost allocation models mapping CPU/memory utilization to real-time cloud invoice line items, reducing idle cluster over-provisioning by 38%.',
    Citation_Count__c = 54,
    Open_Access_URL__c = 'https://arxiv.org/abs/2309.08129',
    PDF_URL__c = 'https://arxiv.org/pdf/2309.08129.pdf',
    Primary_Discipline__c = 'Cloud Computing'
));

// P20
papers.add(new Research_Paper__c(
    Name = 'Direct Access Disaggregated Memory for Cloud-Scale ML Serving',
    Title__c = 'Direct Access Disaggregated Memory for Cloud-Scale ML Serving',
    Authors__c = 'Zhenyuan Ruan, Malte Schwarzkopf, Marcos K. Aguilera, Adam Belay',
    DOI__c = '10.5555/3489146.3489162',
    Publication_Year__c = 2022,
    Venue__c = 'USENIX Annual Technical Conference (ATC)',
    Abstract__c = 'A CXL-enabled memory fabric that permits transformer KV-caches to be stored in shared remote DRAM pools, doubling serving batch throughput without reallocating GPU memory.',
    Citation_Count__c = 138,
    Open_Access_URL__c = 'https://www.usenix.org/conference/atc20/presentation/ruan',
    PDF_URL__c = 'https://www.usenix.org/system/files/atc20-ruan.pdf',
    Primary_Discipline__c = 'Distributed Systems'
));

upsert papers DOI__c;
System.debug('Inserted ' + papers.size() + ' Research Papers successfully.');

// Query papers back with IDs
Map<String, Id> paperByDoi = new Map<String, Id>();
for (Research_Paper__c p : [SELECT Id, DOI__c FROM Research_Paper__c]) {
    paperByDoi.put(p.DOI__c, p.Id);
}

// ---------------------------------------------------------
// 2. RESEARCH MAPS (8 comprehensive research topics)
// ---------------------------------------------------------
List<Research_Map__c> maps = new List<Research_Map__c>();

// Map 1
Research_Map__c m1 = new Research_Map__c(
    Topic__c = 'Serverless Elasticity and Cold-Start Mitigation in Multi-Cloud Systems',
    Status__c = 'Synthesized',
    Target_Discipline__c = 'Cloud Computing',
    Synthesis_Summary__c = 'Modern serverless cloud platforms balance microVM initialization latency against idle host compute costs. Consensus favors microVM snapshot restoration (Firecracker) combined with lightweight WebAssembly runtimes (Faasm, WasmEdge). However, significant debate remains regarding memory footprint bloat under high-concurrency burst conditions.'
);
maps.add(m1);

// Map 2
Research_Map__c m2 = new Research_Map__c(
    Topic__c = 'Zero-Trust Security & eBPF Service Meshes in Hybrid Cloud Platforms',
    Status__c = 'Synthesized',
    Target_Discipline__c = 'Cloud Computing',
    Synthesis_Summary__c = 'Microservice architectures are rapidly moving from user-space Envoy sidecar proxies to kernel-level eBPF socket enforcement (Cilium). Cryptographic mTLS identity verification achieves sub-millisecond p99 overhead, though cross-cluster credential rotation under network partitioning is still an active research gap.'
);
maps.add(m2);

// Map 3
Research_Map__c m3 = new Research_Map__c(
    Topic__c = 'Adaptive Kubernetes Orchestration and Energy-Efficient Cluster Bin-Packing',
    Status__c = 'Synthesized',
    Target_Discipline__c = 'Cloud Computing',
    Synthesis_Summary__c = 'Large-scale cluster orchestration has evolved from heuristic first-fit algorithms to network-flow scheduling (Firmament) and machine-learning guided bin-packing. Empirical benchmarks demonstrate a 23-28% reduction in server count without violating SLA bounds.'
);
maps.add(m3);

// Map 4
Research_Map__c m4 = new Research_Map__c(
    Topic__c = 'Carbon-Aware Workload Orchestration across Geo-Distributed Datacenters',
    Status__c = 'Synthesized',
    Target_Discipline__c = 'Cloud Computing',
    Synthesis_Summary__c = 'Dynamic geo-shifting of elastic AI training and batch workloads according to real-time grid carbon emission intensity reduces net greenhouse emissions by 34%. Major trade-offs involve cross-region data transfer egress fees and compliance with data residency regulations.'
);
maps.add(m4);

// Map 5
Research_Map__c m5 = new Research_Map__c(
    Topic__c = 'Edge-to-Cloud Distributed Stream Processing for Autonomous IoT Systems',
    Status__c = 'Synthesized',
    Target_Discipline__c = 'Distributed Systems',
    Synthesis_Summary__c = 'Edge-cloud collaborative computing leverages micro-sandboxes (WasmEdge) to offload real-time stream aggregation to edge gateways, saving up to 60% in WAN telemetry bandwidth while sustaining sub-10ms response times for safety-critical actuators.'
);
maps.add(m5);

// Map 6
Research_Map__c m6 = new Research_Map__c(
    Topic__c = 'Confidential Computing and Hardware Enclaves in Multi-Tenant Public Clouds',
    Status__c = 'Synthesized',
    Target_Discipline__c = 'Cloud Computing',
    Synthesis_Summary__c = 'Hardware-rooted confidential VMs (AMD SEV-SNP, Intel SGX/TDX, SCONE) eliminate trust requirements on cloud hypervisors and infrastructure admins. Memory encryption overhead sits at 4-7% for compute workloads, but storage paging and nested page faults remain bottlenecks.'
);
maps.add(m6);

// Map 7
Research_Map__c m7 = new Research_Map__c(
    Topic__c = 'Multi-Cloud FinOps: Automated Spot Instance Arbitrage and Cost Prediction',
    Status__c = 'Synthesized',
    Target_Discipline__c = 'Cloud Computing',
    Synthesis_Summary__c = 'Cross-cloud spot instance arbitrage systems exploit price discrepancies between AWS, GCP, and Azure spot markets. Using proactive preemption forecasting, checkpoint-restore cycles achieve 50-60% cloud cost reduction for batch analytics.'
);
maps.add(m7);

// Map 8
Research_Map__c m8 = new Research_Map__c(
    Topic__c = 'Disaggregated Cloud Memory and CXL Interconnects for Large-Scale AI Training',
    Status__c = 'In Progress',
    Target_Discipline__c = 'Distributed Systems',
    Synthesis_Summary__c = 'Disaggregated memory over CXL switches tackles the DRAM stranding problem in multi-tenant datacenters. By pooling memory across server racks, ML serving latency and GPU idling drop significantly despite non-uniform memory access NUMA characteristics.'
);
maps.add(m8);

insert maps;
System.debug('Inserted ' + maps.size() + ' Research Maps successfully.');

// ---------------------------------------------------------
// 3. MAP-PAPER LINKS (Connecting papers with relevance scores)
// ---------------------------------------------------------
List<Map_Paper_Link__c> links = new List<Map_Paper_Link__c>();

// Map 1 links
links.add(new Map_Paper_Link__c(Research_Map__c = m1.Id, Research_Paper__c = paperByDoi.get('10.1145/3419111.3421285'), Relevance_Score__c = 98.0, Inclusion_Rationale__c = 'Foundational empirical study on multi-tenant serverless cold starts.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m1.Id, Research_Paper__c = paperByDoi.get('10.5555/3342195.3387542'), Relevance_Score__c = 95.5, Inclusion_Rationale__c = 'Defines the modern microVM architecture used by AWS Lambda and Fargate.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m1.Id, Research_Paper__c = paperByDoi.get('10.5555/3489146.3489178'), Relevance_Score__c = 92.0, Inclusion_Rationale__c = 'Stateful serverless WebAssembly isolation architecture.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m1.Id, Research_Paper__c = paperByDoi.get('10.1109/IC2E52221.2023.00018'), Relevance_Score__c = 87.5, Inclusion_Rationale__c = 'Ultra-low startup latency benchmarks for lightweight function execution.'));

// Map 2 links
links.add(new Map_Paper_Link__c(Research_Map__c = m2.Id, Research_Paper__c = paperByDoi.get('10.1145/3548606.3560610'), Relevance_Score__c = 99.0, Inclusion_Rationale__c = 'Primary evaluation of mTLS performance in hybrid cloud microservices.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m2.Id, Research_Paper__c = paperByDoi.get('10.1145/3544216.3544230'), Relevance_Score__c = 96.0, Inclusion_Rationale__c = 'Establishes sidecar-free eBPF networking performance benchmarks.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m2.Id, Research_Paper__c = paperByDoi.get('10.1145/3472883.3473180'), Relevance_Score__c = 94.0, Inclusion_Rationale__c = 'Production deployment analysis of Cilium eBPF mesh at scale.'));

// Map 3 links
links.add(new Map_Paper_Link__c(Research_Map__c = m3.Id, Research_Paper__c = paperByDoi.get('10.1109/TCC.2024.3129841'), Relevance_Score__c = 97.0, Inclusion_Rationale__c = 'Modern adaptive pod scheduling algorithms for Kubernetes.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m3.Id, Research_Paper__c = paperByDoi.get('10.1145/2741948.2741964'), Relevance_Score__c = 93.0, Inclusion_Rationale__c = 'Google Borg cluster manager architecture baseline.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m3.Id, Research_Paper__c = paperByDoi.get('10.5555/3026877.3026886'), Relevance_Score__c = 91.0, Inclusion_Rationale__c = 'Network flow cluster scheduling providing sub-20ms optimal placements.'));

// Map 4 links
links.add(new Map_Paper_Link__c(Research_Map__c = m4.Id, Research_Paper__c = paperByDoi.get('10.1145/3639478.3640021'), Relevance_Score__c = 98.5, Inclusion_Rationale__c = 'Real-time carbon-aware multi-region workload shifting model.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m4.Id, Research_Paper__c = paperByDoi.get('10.1145/3575693.3575701'), Relevance_Score__c = 96.0, Inclusion_Rationale__c = 'Google carbon-intelligent platform methodology and grid metrics.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m4.Id, Research_Paper__c = paperByDoi.get('10.1145/3488659.3493776'), Relevance_Score__c = 90.0, Inclusion_Rationale__c = 'Carbon footprint of AI foundation model cloud training.'));

// Map 5 links
links.add(new Map_Paper_Link__c(Research_Map__c = m5.Id, Research_Paper__c = paperByDoi.get('10.1109/IC2E52221.2023.00018'), Relevance_Score__c = 95.0, Inclusion_Rationale__c = 'WasmEdge runtime benchmark for edge stream processing.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m5.Id, Research_Paper__c = paperByDoi.get('10.1109/MWC.2021.9360871'), Relevance_Score__c = 92.5, Inclusion_Rationale__c = 'Smart city distributed edge orchestration system architecture.'));

// Map 6 links
links.add(new Map_Paper_Link__c(Research_Map__c = m6.Id, Research_Paper__c = paperByDoi.get('10.1109/SP46215.2024.1053142'), Relevance_Score__c = 97.0, Inclusion_Rationale__c = 'AMD SEV-SNP and Intel TDX confidential VM performance study.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m6.Id, Research_Paper__c = paperByDoi.get('10.5555/3026877.3026922'), Relevance_Score__c = 94.0, Inclusion_Rationale__c = 'SCONE secure container runtime using hardware enclaves.'));

// Map 7 links
links.add(new Map_Paper_Link__c(Research_Map__c = m7.Id, Research_Paper__c = paperByDoi.get('10.1145/3627703.3629581'), Relevance_Score__c = 98.0, Inclusion_Rationale__c = 'Predictive multi-cloud spot arbitrage reinforcement learning model.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m7.Id, Research_Paper__c = paperByDoi.get('10.1145/3542929.3563478'), Relevance_Score__c = 94.0, Inclusion_Rationale__c = 'Cloud FinOps Kubernetes container cost allocation and right-sizing.'));

// Map 8 links
links.add(new Map_Paper_Link__c(Research_Map__c = m8.Id, Research_Paper__c = paperByDoi.get('10.1145/3563766.3564082'), Relevance_Score__c = 96.5, Inclusion_Rationale__c = 'CXL pooled memory datacenter architecture and DRAM savings.'));
links.add(new Map_Paper_Link__c(Research_Map__c = m8.Id, Research_Paper__c = paperByDoi.get('10.5555/3489146.3489162'), Relevance_Score__c = 95.0, Inclusion_Rationale__c = 'Disaggregated DRAM for cloud transformer model inference.'));

insert links;
System.debug('Inserted ' + links.size() + ' Map-Paper Links successfully.');

// ---------------------------------------------------------
// 4. EXTRACTED METRICS (Realistic benchmark data)
// ---------------------------------------------------------
List<Extracted_Metric__c> metrics = new List<Extracted_Metric__c>();

metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3419111.3421285'), Metric_Name__c = 'P99 Cold-Start Latency', Metric_Value__c = 184.2, Unit__c = 'ms', Benchmark_Dataset__c = 'AWS Lambda Microbenchmarks'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3419111.3421285'), Metric_Name__c = 'Memory Reduction via Pre-warming', Metric_Value__c = 42.5, Unit__c = '%', Benchmark_Dataset__c = 'Firecracker Snapshot Pool'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.5555/3342195.3387542'), Metric_Name__c = 'MicroVM Boot Time', Metric_Value__c = 4.8, Unit__c = 'ms', Benchmark_Dataset__c = 'Firecracker KVM VMM Suite'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.5555/3342195.3387542'), Metric_Name__c = 'Base Memory Overhead', Metric_Value__c = 5.2, Unit__c = 'MB', Benchmark_Dataset__c = 'AWS Production Fleet Telemetry'));

metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3548606.3560610'), Metric_Name__c = 'eBPF mTLS Handshake Overhead', Metric_Value__c = 0.88, Unit__c = 'ms', Benchmark_Dataset__c = 'Cilium Cryptographic Mesh'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3544216.3544230'), Metric_Name__c = 'Sidecar-Free Throughput Gain', Metric_Value__c = 48.0, Unit__c = '%', Benchmark_Dataset__c = 'DeathStarBench Social Network'));

metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1109/TCC.2024.3129841'), Metric_Name__c = 'Cluster Node Density Improvement', Metric_Value__c = 23.4, Unit__c = '%', Benchmark_Dataset__c = 'Google Cluster Traces 2019'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.5555/3026877.3026886'), Metric_Name__c = 'Scheduling Placement Latency', Metric_Value__c = 14.5, Unit__c = 'ms', Benchmark_Dataset__c = 'Firmament 10k Task Batch'));

metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3639478.3640021'), Metric_Name__c = 'Grid Carbon Emission Abatement', Metric_Value__c = 34.0, Unit__c = '%', Benchmark_Dataset__c = 'Electricity Maps Global Grid'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3575693.3575701'), Metric_Name__c = 'Hourly Carbon Tracking Efficiency', Metric_Value__c = 91.2, Unit__c = '%', Benchmark_Dataset__c = 'Google Datacenter Energy Logs'));

metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1109/IC2E52221.2023.00018'), Metric_Name__c = 'Cold Startup Time (Wasm)', Metric_Value__c = 45.0, Unit__c = 'microseconds', Benchmark_Dataset__c = 'WasmEdge vs Docker Baseline'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1109/SP46215.2024.1053142'), Metric_Name__c = 'Confidential Memory Encryption Penalty', Metric_Value__c = 6.2, Unit__c = '%', Benchmark_Dataset__c = 'SPECrate 2017 Benchmark'));

metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3627703.3629581'), Metric_Name__c = 'Spot Cloud Cost Savings', Metric_Value__c = 58.4, Unit__c = '%', Benchmark_Dataset__c = 'AWS EC2 Spot Price History'));
metrics.add(new Extracted_Metric__c(Research_Paper__c = paperByDoi.get('10.1145/3563766.3564082'), Metric_Name__c = 'Stranded DRAM Reduction', Metric_Value__c = 14.1, Unit__c = '%', Benchmark_Dataset__c = 'Microsoft Azure Cluster Traces'));

insert metrics;
System.debug('Inserted ' + metrics.size() + ' Extracted Metrics successfully.');

// ---------------------------------------------------------
// 5. RESEARCH FINDINGS (Verified academic empirical claims)
// ---------------------------------------------------------
List<Research_Finding__c> findings = new List<Research_Finding__c>();

findings.add(new Research_Finding__c(
    Research_Map__c = m1.Id,
    Research_Paper__c = paperByDoi.get('10.1145/3419111.3421285'),
    Claim_Summary__c = 'Memory pre-warming cuts P99 cold-start latency from 580ms to 184ms.',
    Exact_Quote__c = 'By maintaining an in-memory page tree of common runtime libraries, container initialization dropped from 580ms to 184ms across ten thousand test trials.',
    Page_Number__c = 4,
    Section_Name__c = '4.2 Evaluation of Warm-Start Page Sharing',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 99.4
));

findings.add(new Research_Finding__c(
    Research_Map__c = m1.Id,
    Research_Paper__c = paperByDoi.get('10.5555/3342195.3387542'),
    Claim_Summary__c = 'Minimalist VMM implementation launches microVMs in under 5 milliseconds.',
    Exact_Quote__c = 'Firecracker creates and starts a microVM in less than 5 milliseconds, consuming approximately 5 MiB of memory overhead per instance.',
    Page_Number__c = 3,
    Section_Name__c = '3. Architecture and Implementation',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 99.8
));

findings.add(new Research_Finding__c(
    Research_Map__c = m2.Id,
    Research_Paper__c = paperByDoi.get('10.1145/3548606.3560610'),
    Claim_Summary__c = 'Kernel sockops redirection bypasses TCP stacks, yielding 0.88ms p99 response times.',
    Exact_Quote__c = 'Kernel-level sockops redirection eliminates user-space context switches for service mesh proxies, achieving p99 response times of 1.15ms.',
    Page_Number__c = 6,
    Section_Name__c = '6. Sidecar-Free Service Mesh Benchmarks',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 98.2
));

findings.add(new Research_Finding__c(
    Research_Map__c = m2.Id,
    Research_Paper__c = paperByDoi.get('10.1145/3544216.3544230'),
    Claim_Summary__c = 'Removing per-pod Envoy sidecars doubles microservice throughput.',
    Exact_Quote__c = 'Eliminating sidecar proxy serialization and context switches increased request processing capacity by 48% across DeathStarBench endpoints.',
    Page_Number__c = 5,
    Section_Name__c = '5. Performance Analysis',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 96.5
));

findings.add(new Research_Finding__c(
    Research_Map__c = m3.Id,
    Research_Paper__c = paperByDoi.get('10.1109/TCC.2024.3129841'),
    Claim_Summary__c = 'Dynamic bin-packing lowers cluster node count by 23% without breaching SLAs.',
    Exact_Quote__c = 'Our scheduler packed bursty workloads with 23% fewer compute instances than default Kubernetes kube-scheduler.',
    Page_Number__c = 7,
    Section_Name__c = '5. Experimental Results',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 94.8
));

findings.add(new Research_Finding__c(
    Research_Map__c = m4.Id,
    Research_Paper__c = paperByDoi.get('10.1145/3639478.3640021'),
    Claim_Summary__c = 'Geographic workload shifting reduces carbon emissions by 34% with under 5% SLA impact.',
    Exact_Quote__c = 'Shifting elastic batch processing jobs across geographic cloud datacenters according to real-time grid carbon intensity reduced greenhouse emissions by 34% with under 5% SLA impact.',
    Page_Number__c = 8,
    Section_Name__c = '4. Carbon Abatement Evaluation',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 97.1
));

findings.add(new Research_Finding__c(
    Research_Map__c = m6.Id,
    Research_Paper__c = paperByDoi.get('10.1109/SP46215.2024.1053142'),
    Claim_Summary__c = 'Hardware confidential VM memory encryption adds 6.2% compute overhead.',
    Exact_Quote__c = 'Across standard SPEC CPU benchmarks, AMD SEV-SNP cryptographic page isolation incurred an aggregate execution time penalty of 6.2%.',
    Page_Number__c = 9,
    Section_Name__c = '7. Performance Overhead Characterization',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 98.7
));

findings.add(new Research_Finding__c(
    Research_Map__c = m7.Id,
    Research_Paper__c = paperByDoi.get('10.1145/3627703.3629581'),
    Claim_Summary__c = 'Predictive spot bidding delivers 58.4% cost reductions with zero lost transactions.',
    Exact_Quote__c = 'By migrating stateless worker pools 120 seconds ahead of predicted host reclamations, spot cluster operational expenses fell by 58.4%.',
    Page_Number__c = 11,
    Section_Name__c = '6. FinOps Arbitrage Results',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 96.0
));

findings.add(new Research_Finding__c(
    Research_Map__c = m8.Id,
    Research_Paper__c = paperByDoi.get('10.1145/3563766.3564082'),
    Claim_Summary__c = 'CXL pooled memory cuts stranded datacenter DRAM by 14.1%.',
    Exact_Quote__c = 'Disaggregating DRAM over CXL fabric switches reclaimed 14.1% of stranded server memory capacity across production hypervisor racks.',
    Page_Number__c = 6,
    Section_Name__c = '5. Memory Pooling at Scale',
    Verification_Status__c = 'Verified',
    Confidence_Score__c = 95.3
));

insert findings;
System.debug('Inserted ' + findings.size() + ' Research Findings successfully.');

// ---------------------------------------------------------
// 6. RESEARCH CONFLICTS (Academic debates and trade-offs)
// ---------------------------------------------------------
List<Research_Conflict__c> conflicts = new List<Research_Conflict__c>();

conflicts.add(new Research_Conflict__c(
    Research_Map__c = m1.Id,
    Paper_A__c = paperByDoi.get('10.1145/3419111.3421285'),
    Paper_B__c = paperByDoi.get('10.5555/3342195.3387542'),
    Disagreement_Area__c = 'MicroVM Memory Overcommit Scalability',
    Conflict_Description__c = 'Mehta et al. demonstrate that aggressive memory overcommit leads to heavy swap thrashing during concurrent cold-start waves, while Agache et al. argue that Firecracker zero-copy copy-on-write page sharing supports 10x density without performance cliff.',
    Severity__c = 'Moderate'
));

conflicts.add(new Research_Conflict__c(
    Research_Map__c = m2.Id,
    Paper_A__c = paperByDoi.get('10.1145/3548606.3560610'),
    Paper_B__c = paperByDoi.get('10.1145/3544216.3544230'),
    Disagreement_Area__c = 'eBPF Host Kernel Security vs User-Space Proxy Isolation',
    Conflict_Description__c = 'Al-Mansoor et al. contend that kernel-level eBPF shared security contexts create severe privilege escalation attack surfaces across multi-tenant pods, whereas Graf et al. prove that eBPF BPF verifier guarantees superior security isolation compared to vulnerable user-space sidecar proxies.',
    Severity__c = 'Direct Contradiction'
));

conflicts.add(new Research_Conflict__c(
    Research_Map__c = m3.Id,
    Paper_A__c = paperByDoi.get('10.1109/TCC.2024.3129841'),
    Paper_B__c = paperByDoi.get('10.5555/3026877.3026886'),
    Disagreement_Area__c = 'Centralized Network-Flow vs Decentralized Scheduling Speed',
    Conflict_Description__c = 'Gog et al. show that centralized min-cost max-flow graph algorithms compute optimal placements in 15ms, whereas Rostova et al. present benchmarks demonstrating that network-flow graphs collapse under churn rates exceeding 5,000 pods per minute.',
    Severity__c = 'Moderate'
));

conflicts.add(new Research_Conflict__c(
    Research_Map__c = m4.Id,
    Paper_A__c = paperByDoi.get('10.1145/3639478.3640021'),
    Paper_B__c = paperByDoi.get('10.1145/3488659.3493776'),
    Disagreement_Area__c = 'WAN Data Egress Carbon vs Cloud Compute Energy Savings',
    Conflict_Description__c = 'Sundaram et al. argue cross-region model checkpoint migration is carbon-negative, while Patterson et al. measure network router and fiber optic transmission energy proving that cross-continent transfer of 100GB+ datasets cancels out grid green gains.',
    Severity__c = 'Direct Contradiction'
));

conflicts.add(new Research_Conflict__c(
    Research_Map__c = m6.Id,
    Paper_A__c = paperByDoi.get('10.1109/SP46215.2024.1053142'),
    Paper_B__c = paperByDoi.get('10.5555/3026877.3026922'),
    Disagreement_Area__c = 'Confidential Enclave I/O Trapping Latency',
    Conflict_Description__c = 'Parno et al. report that hardware confidential VM storage I/O suffers up to a 34% throughput drop from hypervisor bounce buffering, whereas Arnautov et al. demonstrate that asynchronous system call shielding within SCONE achieves near-native I/O throughput.',
    Severity__c = 'Moderate'
));

insert conflicts;
System.debug('Inserted ' + conflicts.size() + ' Research Conflicts successfully.');

// ---------------------------------------------------------
// 7. RESEARCH GAPS (Open research problems and experiments)
// ---------------------------------------------------------
List<Research_Gap__c> gaps = new List<Research_Gap__c>();

gaps.add(new Research_Gap__c(
    Research_Map__c = m1.Id,
    Problem_Statement__c = 'Lack of hardware-assisted memory snapshotting across heterogeneous ARM and x86 cloud nodes.',
    Proposed_Experiment__c = 'Benchmark cross-architecture snapshot migration using unified memory pages between Graviton3 and AMD EPYC servers under synthetic financial micro-benchmarks.',
    Priority__c = 'High',
    Estimated_Complexity__c = 'High',
    Status__c = 'Experiment Drafted'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m1.Id,
    Problem_Statement__c = 'Predictive pre-warming algorithms over-allocate memory by 35% during unpredictable diurnal load transitions.',
    Proposed_Experiment__c = 'Implement an adaptive LSTM-Kalman hybrid predictor trained on Azure Functions 2021 traces to dynamically adjust warmup pool sizes.',
    Priority__c = 'Medium',
    Estimated_Complexity__c = 'Medium',
    Status__c = 'Identified'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m2.Id,
    Problem_Statement__c = 'Cross-cluster zero-trust token rotation causes intermittent connection drops during multi-cloud failover.',
    Proposed_Experiment__c = 'Design an asynchronous distributed Raft-based session ticket cache that pre-propagates mutual TLS certificates across AWS and GCP 45 seconds prior to cutover.',
    Priority__c = 'High',
    Estimated_Complexity__c = 'High',
    Status__c = 'In Review'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m3.Id,
    Problem_Statement__c = 'Current Kubernetes scheduler heuristics fail to account for CPU thermal throttling in high-density rack deployments.',
    Proposed_Experiment__c = 'Instrument IPMI chassis thermal telemetry directly into kube-scheduler node scoring plugins and measure node lifespan and power draw.',
    Priority__c = 'Medium',
    Estimated_Complexity__c = 'Low',
    Status__c = 'Identified'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m4.Id,
    Problem_Statement__c = 'Absence of standardized real-time marginal carbon emission API standards across international cloud regions.',
    Proposed_Experiment__c = 'Deploy synthetic probes polling European Entso-E and US CAISO telemetry every 60 seconds to quantify discrepancy between average vs marginal emissions.',
    Priority__c = 'High',
    Estimated_Complexity__c = 'Medium',
    Status__c = 'Experiment Drafted'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m5.Id,
    Problem_Statement__c = 'Intermittent WAN backhaul latency spikes cause out-of-order stream processing at edge gateways.',
    Proposed_Experiment__c = 'Evaluate vector clock watermarking with dynamic buffer resizing on edge devices during simulated 4G/5G cell handoffs.',
    Priority__c = 'Medium',
    Estimated_Complexity__c = 'Medium',
    Status__c = 'Identified'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m6.Id,
    Problem_Statement__c = 'Side-channel cache attacks on encrypted memory enclaves in shared public cloud hypervisors.',
    Proposed_Experiment__c = 'Execute prime-and-probe cache timing attacks against AMD SEV-SNP virtual machines during active AES-GCM encryption streams.',
    Priority__c = 'High',
    Estimated_Complexity__c = 'High',
    Status__c = 'In Review'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m7.Id,
    Problem_Statement__c = 'Multi-cloud egress pricing models obscure the true total cost of ownership of spot arbitrage.',
    Proposed_Experiment__c = 'Construct an automated billing simulator integrating AWS Direct Connect and GCP Cloud Interconnect tariffs into spot bidding algorithms.',
    Priority__c = 'Medium',
    Estimated_Complexity__c = 'Low',
    Status__c = 'Addressed'
));

gaps.add(new Research_Gap__c(
    Research_Map__c = m8.Id,
    Problem_Statement__c = 'Cache coherence protocols over CXL 3.0 switches suffer from non-deterministic latency spikes during multi-node LLM gradient synchronization.',
    Proposed_Experiment__c = 'Run 70B parameter LLaMA-2 model training over simulated 8-node CXL switch fabric with varying memory pooling ratios and measure step time.',
    Priority__c = 'High',
    Estimated_Complexity__c = 'High',
    Status__c = 'Experiment Drafted'
));

insert gaps;
System.debug('Inserted ' + gaps.size() + ' Research Gaps successfully.');

System.debug('=== Comprehensive Research Data Seeding Complete! ===');
