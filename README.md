# ChromaDB + LLM Integration for RAG System

## Overview

This repository demonstrates the integration of **ChromaDB** with a **Large Language Model (LLM)** to implement a simple **Retrieval-Augmented Generation (RAG)** system. The goal is to enhance the LLM's ability to provide accurate and contextually relevant responses by retrieving relevant data from a vector database.

## Features

- **Vector Database Creation**:  
  ChromaDB is used to create and manage the vector database, enabling efficient storage and retrieval of embeddings.
  
- **Integration with LLM**:  
  A pre-trained LLM is integrated to generate human-like responses using the retrieved contextual data.
  
- **Retrieval-Augmented Generation (RAG)**:  
  Combines the strengths of retrieval-based systems and generative models to provide more informed and relevant outputs.

## Use Case

The implemented system can be used in applications such as:
- Chatbots with domain-specific knowledge.
- Question-answering systems that require retrieval from custom datasets.
- Document search and summarization.

## Workflow

1. **Data Ingestion**:  
   A dataset of simple text files in the "Test_Data" is preprocessed and stored in the ChromaDB vector database after generating embeddings.
   
2. **Query Handling**:  
   When a query is received, the system retrieves relevant data from the vector database based on similarity.

3. **LLM Integration**:  
   The retrieved context is passed to the LLM, which generates a response augmented with the additional information.

4. **Output Generation**:  
   The final response is returned to the user, blending retrieval-based precision with generative flexibility.

## Tech Stack

- **ChromaDB**: Vector database for efficient embedding storage and retrieval.
- **LLM**: Integrated with an open-source or proprietary model (e.g., OpenAI GPT, Hugging Face Transformers).
- **Python**: Core programming language for the implementation.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   conda create --name chroma-llm-rag python=3.10.15
   git clone https://github.com/ThisIsFarhan/chroma-llm-rag.git
   cd chroma-llm-rag
