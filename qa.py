import streamlit as st
import openai

# Authenticate with the OpenAI API key
openai.api_key = st.secrets.openai.api_key


def create_prompt(context,query):
    header = "You are an expert on East African countries. Answer the question and you can deviate from the provided context if neccessary, and if the answer is not contained within the text and requires some latest information to be updated, print 'Sorry Not Sufficient context to answer query' \n"
    return header + context + "\n\n" + query + "\n"

def generate_answer(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.8,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop = [' END']
    )
    return (response.choices[0].text).strip()
