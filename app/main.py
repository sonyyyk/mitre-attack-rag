from app.embeddings.manager import EmbeddingManager
from app.mitre.parser import MITREParser


def main():

    parser = MITREParser()

    manager = EmbeddingManager()

    if manager.embeddings_exist():

        print("Loading embeddings from disk...")

        embeddings = manager.load_embeddings()

    else:

        techniques = parser.parse_all_attack_patterns()

        embeddings = manager.create_embeddings(
            techniques
        )

        manager.save_embeddings(
            embeddings
        )

        print("Embeddings saved.")

    print()

    print(f"Loaded embeddings: {len(embeddings)}")

    print(f"Embedding dimension: {len(embeddings[0])}")


if __name__ == "__main__":
    main()