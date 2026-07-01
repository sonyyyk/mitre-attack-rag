from app.embeddings.manager import EmbeddingManager
from app.mitre.parser import MITREParser
from app.vector_db.manager import VectorDBManager


def main():

    print("=" * 70)
    print("MITRE ATT&CK Vector Database Builder")
    print("=" * 70)

    print("\nLoading MITRE techniques...")

    parser = MITREParser()

    techniques = parser.parse_all_attack_patterns()

    print(f"Loaded techniques: {len(techniques)}")

    print("\nLoading embeddings...")

    embedding_manager = EmbeddingManager()

    embeddings = embedding_manager.load_embeddings()

    print(f"Loaded embeddings: {len(embeddings)}")

    print("\nConnecting to ChromaDB...")

    vector_db = VectorDBManager()

    # Якщо база вже існує — очистити її
    vector_db.clear()

    print("Creating vector database...")

    vector_db.add_documents(
        techniques=techniques,
        embeddings=embeddings,
    )

    print("\nDatabase successfully created!")

    print(f"Stored vectors: {vector_db.count()}")

    print("=" * 70)


if __name__ == "__main__":
    main()