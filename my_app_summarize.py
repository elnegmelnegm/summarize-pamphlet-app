import streamlit as st
image_path = 'https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png'
st.image(image_path)

st.title("Pamphlet Summarization App")
st.subheader("A web application that allows to summarize pamphlets")

# Text input
txt_input = st.text_area('Enter your text', '', height=200)
from transformers import pipeline

get_completion = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize(txt_input):
    output = get_completion(txt_input)
    return output[0]['summary_text']

if st.button('Submit'):
    summary = summarize(txt_input)
    st.write(summary)
