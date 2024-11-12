import os
import chromadb
from chromadb.utils import embedding_functions

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

chromaclient = chromadb.PersistentClient(path="./db/chromaStorage")
embeddingFunc = embedding_functions.DefaultEmbeddingFunction()
collection = chromaclient.get_or_create_collection(
    name="doc_qa_collection", embedding_function=embeddingFunc
)

#Run the setup for the first time and comment for later use
#----------------------------INIT SETUP----------------------------------------------
# #Function for loading the document contents
# def loadDoc(path):
#     documents = []
#     for filename in os.listdir(path):
#         if filename.endswith(".txt"):
#             with open(os.path.join(path, filename)) as file:
#                 documents.append({"id": filename, "text":file.read()})
#     return documents

# #Function for making the chunks of the data
# def split(text, chunk_size = 150, chunk_overlap = 2):
#     chunks = []
#     start = 0
#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start = end - chunk_overlap
#     return chunks


# documents = loadDoc("./Test_Data/")

# chunked_docs = []
# for doc in documents:
#     chunks = split(doc['text'])
#     for idx, chunk in enumerate(chunks):
#         chunked_docs.append({"id": f"{doc['id']}_chunk{idx+1}", "text": chunk})

# for doc in chunked_docs:
#     doc["embedding"] = embeddingFunc([doc["text"]])


# for doc in chunked_docs:
#     collection.upsert(documents=doc["text"], ids=doc["id"], embeddings=doc["embedding"])
#-------------------------------------END OF INIT SETUP----------------------------------------------


llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key = "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",
    temperature=0,
)

def get_relevant_chunks(question, n_answers = 2):
    result = collection.query(query_texts=question, n_results=n_answers)
    relchunks = []
    for chunk in result["documents"][0]:
        relchunks.append(chunk)
    return relchunks

def getResponse(question, context):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful question-answer system. Use the following pieces of retrieved text to answer the question asked by the user. Keep the answer concise and upto 3 to 4 sentences. If you dont know the answer, just say you dont know. {cont}"),
        ("human", "{ques}"),
    ])

    chain = prompt_template | llm | StrOutputParser()
    response = chain.invoke({"cont" : context, "ques": question})
    return response


#Testing- Asking questions related to the AI-generated fictional articles
query = "what was the bold move towards renewable energy?"
chunks = get_relevant_chunks(query)
context = "\n\n".join(chunks)
print(getResponse(question=query, context=context))