import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

documents = [
    {"id":"doc1", "text":"My name is Farhan"},
    {"id":"doc2", "text":"Hello World"},
    {"id":"doc3", "text":"I like to go to gym"},
]

for doc in documents:
    collection.upsert(documents=[doc["text"]], ids=doc["id"])

query = "Gym is good"

results = collection.query(
    query_texts=query,
    n_results=3
)

for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(
        f" For the query: {query}, \n Found similar document: {document} (ID: {doc_id}, Distance: {distance})"
    )
