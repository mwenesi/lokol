import streamlit as st
from vector_search import *
from utils import *
import qa

st.sidebar.markdown('<h3>Add a website link</h3>', unsafe_allow_html=True)

url = st.sidebar.text_input("Enter the url of the document")


if st.sidebar.button("Update Database") and url:
    with st.spinner("Updating Database..."):
        corpusData = scrape_text_from_url(url)
        addData(corpusData,url)
        st.sidebar.success("Database Updated")

st.markdown('<h1 style="text-align: center">AskAbu</h1>', unsafe_allow_html=True)
st.markdown('<h9 style="text-align: center">GTP Search Engine for Businesses</h9>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

st.markdown('<h3 style="text-align: center">Ask a Question</h3>', unsafe_allow_html=True)

query = st.text_input("Enter your question")
button = st.button("Submit")

if button and query:
    with st.spinner("Searching for the answer..."):
        urls,res = find_match(query,2)
        context= "\n\n".join(res)
        st.expander("Context").write(context)
        prompt = qa.create_prompt(context,query)
        answer = qa.generate_answer(prompt)
        st.success("Answer: "+answer)
