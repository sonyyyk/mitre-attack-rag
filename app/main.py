from collections import defaultdict

from app.embeddings.manager import EmbeddingManager
from app.ml.manager import MLManager
from app.mitre.parser import MITREParser


def main():
    print("Loading MITRE techniques...")

    parser = MITREParser()
    techniques = parser.parse_all_attack_patterns()

    print(f"Loaded techniques: {len(techniques)}")

    print("\nLoading embeddings...")

    embedding_manager = EmbeddingManager()
    embeddings = embedding_manager.load_embeddings()

    print(f"Loaded embeddings: {len(embeddings)}")

    print("\nRunning KMeans clustering...")

    ml_manager = MLManager()
    clusters = ml_manager.cluster_embeddings(embeddings)

    print("Clustering completed.\n")

    grouped = defaultdict(list)

    for technique, cluster in zip(techniques, clusters):
        grouped[cluster].append(technique)

    print("=" * 70)
    print("MITRE ATT&CK Technique Clusters")
    print("=" * 70)

    for cluster_id in sorted(grouped.keys()):

        print(f"\nCluster {cluster_id}")
        print("-" * 70)

        for technique in grouped[cluster_id][:15]:
            print(f"• {technique.mitre_id} - {technique.name}")

        if len(grouped[cluster_id]) > 15:
            print("...")

        print(f"\nTotal techniques: {len(grouped[cluster_id])}")

    print("\n" + "=" * 70)
    print("Cluster Statistics")
    print("=" * 70)

    for cluster_id in sorted(grouped.keys()):
        print(f"Cluster {cluster_id}: {len(grouped[cluster_id])} techniques")


if __name__ == "__main__":
    main()