from app.embeddings.encoder import EmbeddingEncoder
from app.vector_db.manager import VectorDBManager


def main():

    encoder = EmbeddingEncoder()

    vector_db = VectorDBManager()

    query = """
    The attacker dumped credentials from LSASS memory.
    """

    print()
    print("Query:")
    print(query)
    print()

    results = vector_db.search_text(
        query,
        encoder,
        top_k=5,
    )

    print("=" * 70)
    print("Top 5 similar MITRE techniques")
    print("=" * 70)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for index in range(len(documents)):

        print()
        print(f"Rank #{index + 1}")
        print("-" * 50)

        print("Technique:")
        print(metadatas[index]["name"])

        print()

        print("Distance:")
        print(distances[index])

        print()

        print("Document:")
        print(documents[index][:250])
        print("...")


if __name__ == "__main__":
    main()