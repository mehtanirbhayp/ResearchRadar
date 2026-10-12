import os
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 1. Papers CSV
papers = [
    {
        "Name": "Serverless Cold-Start Analysis in Multi-Tenant Clouds",
        "Title__c": "Serverless Cold-Start Analysis in Multi-Tenant Clouds",
        "Authors__c": "Nirbhay Mehta, Sarah Jenkins, David K. Miller",
        "DOI__c": "10.1145/3419111.3421285",
        "Publication_Year__c": 2023,
        "Venue__c": "ACM Symposium on Cloud Computing (SoCC)",
        "Abstract__c": "Serverless Function-as-a-Service (FaaS) offers fine-grained elasticity but suffers from container initialization latency (cold-starts). We analyze memory-aware pre-warming and snapshot restoration across 10,000 invocations.",
        "Citation_Count__c": 142,
        "Open_Access_URL__c": "https://arxiv.org/abs/2301.04182",
        "PDF_URL__c": "https://arxiv.org/pdf/2301.04182.pdf",
        "Primary_Discipline__c": "Cloud Computing"
    },
    {
        "Name": "Adaptive Resource Scheduling for Kubernetes Clusters",
        "Title__c": "Adaptive Resource Scheduling for Kubernetes Clusters",
        "Authors__c": "Elena Rostova, Amit Patel, Marcus Vance",
        "DOI__c": "10.1109/TCC.2024.3129841",
        "Publication_Year__c": 2024,
        "Venue__c": "IEEE Transactions on Cloud Computing",
        "Abstract__c": "Dynamic pod placement algorithms minimizing resource fragmentation while maintaining SLA compliance for batch and streaming workloads in heterogeneous cloud environments.",
        "Citation_Count__c": 89,
        "Open_Access_URL__c": "https://arxiv.org/abs/2402.09112",
        "PDF_URL__c": "https://arxiv.org/pdf/2402.09112.pdf",
        "Primary_Discipline__c": "Cloud Computing"
    },
    {
        "Name": "Zero-Trust Architecture in Hybrid Cloud Microservices",
        "Title__c": "Zero-Trust Architecture in Hybrid Cloud Microservices",
        "Authors__c": "Tariq Al-Mansoor, Li Wei, Brenda Cooper",
        "DOI__c": "10.1145/3548606.3560610",
        "Publication_Year__c": 2023,
        "Venue__c": "ACM Conference on Computer and Communications Security (CCS)",
        "Abstract__c": "Evaluates mutual TLS (mTLS) overhead with eBPF service meshes in hybrid-cloud deployments, demonstrating cryptographic identity verification with sub-millisecond p99 latency.",
        "Citation_Count__c": 210,
        "Open_Access_URL__c": "https://arxiv.org/abs/2305.10984",
        "PDF_URL__c": "https://arxiv.org/pdf/2305.10984.pdf",
        "Primary_Discipline__c": "Cloud Computing"
    },
    {
        "Name": "Carbon-Aware Workload Orchestration across Global Cloud Regions",
        "Title__c": "Carbon-Aware Workload Orchestration across Global Cloud Regions",
        "Authors__c": "Kavita Sundaram, Lucas Dupont, Hans Gruber",
        "DOI__c": "10.1145/3639478.3640021",
        "Publication_Year__c": 2025,
        "Venue__c": "USENIX Conference on Operational Systems & Cloud",
        "Abstract__c": "Shifting elastic batch processing jobs across geographic cloud datacenters according to real-time grid carbon intensity reduced greenhouse emissions by 34% with under 5% SLA impact.",
        "Citation_Count__c": 34,
        "Open_Access_URL__c": "https://arxiv.org/abs/2501.07721",
        "PDF_URL__c": "https://arxiv.org/pdf/2501.07721.pdf",
        "Primary_Discipline__c": "Cloud Computing"
    }
]

with open(os.path.join(DATA_DIR, "Research_Paper__c.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(papers[0].keys()))
    writer.writeheader()
    writer.writerows(papers)

print("Generated sample data CSVs in salesforce/data/!")
