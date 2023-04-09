import pinecone
from sentence_transformers import SentenceTransformer,util
import streamlit as st

model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone_config = st.secrets["Pinecone"]
api_key = pinecone_config["PINECONE_API_KEY"]
environment = pinecone_config["PINECONE_ENVIRONMENT"]
index_name = pinecone_config["PINECONE_INDEX_NAME"]

# Initialize Pinecone
pinecone.init(api_key=api_key, environment=environment)

# Get the index
index = pinecone.Index(index_name)

def addData(corpusData,url):
    id = id = index.describe_index_stats()['total_vector_count']
    for i in range(len(corpusData)):
        chunk=corpusData[i]
        chunkInfo=(str(id+i),
                model.encode(chunk).tolist(),
                {'title': url,'context': chunk})
        index.upsert(vectors=[chunkInfo])

def find_match(query,k):
    query_em = model.encode(query).tolist()
    result = index.query(query_em, top_k=k, includeMetadata=True)
    
    return [result['matches'][i]['metadata']['title'] for i in range(k)],[result['matches'][i]['metadata']['context'] for i in range(k)]
import pinecone
from sentence_transformers import SentenceTransformer,util
model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone.init(api_key="f174c324-e266-4d94-9796-555feb361470", environment="us-west4-gcp") 
index = pinecone.Index("tasks")

def addData(corpusData,url):
    id = id = index.describe_index_stats()['total_vector_count']
    for i in range(len(corpusData)):
        chunk=corpusData[i]
        chunkInfo=(str(id+i),
                model.encode(chunk).tolist(),
                {'title': url,'context': chunk})
        index.upsert(vectors=[chunkInfo])

def find_match(query,k):
    query_em = model.encode(query).tolist()
    result = index.query(query_em, top_k=k, includeMetadata=True)
    
    return [result['matches'][i]['metadata']['title'] for i in range(k)],[result['matches'][i]['metadata']['context'] for i in range(k)]