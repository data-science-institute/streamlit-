import streamlit as st
import torch
from transformers import pipeline

st.title("英語文章要約AI")

text = st.text_area("英語の文章を入力してください", placeholder="Write Here")

if st.button("要約"):
    "\n"
    with st.spinner("要約中..."):
        pipe = pipeline("summarization")
        result = pipe(text, max_length=130, min_length=30)
    container = st.container()
    container.write("要約結果")
    st.success(result[0]["summary_text"])
