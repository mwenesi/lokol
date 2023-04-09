import streamlit as st
from io import StringIO
from vector_search import *
from utils import *
import qa

st.markdown('<h1 style="text-align: center">AskAbu</h1>', unsafe_allow_html=True)
st.markdown('<h9 style="text-align: center">GTP Search Engine for Businesses</h9>', unsafe_allow_html=True)

url = False
index = ""
query = False

options = st.radio(
    'Choose task',
    ('Ask a question','Update your Database'))

if 'Update the Database' in options:
    url = st.text_input("Enter the url of the document")
    
if 'Ask a question' in options:
    query = st.text_input("Enter your question")

button = st.button("Submit")
  
if button and (url or query):
    if 'Update the Database' in options:
        with st.spinner("Updating Database..."):
            corpusData = scrape_text_from_url(url)
            addData(corpusData,url)
            st.success("Database Updated")
    if 'Ask a question' in options:
        with st.spinner("Searching for the answer..."):
            urls,res = find_match(query,2)
            context= "\n\n".join(res)
            st.expander("Context").write(context)
            prompt = qa.prompt(context,query)
            answer = qa.generate_answer(prompt)
            st.success("Answer: "+answer)

            
            


       