import streamlit as st
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

@st.cache_resource
def load_model():
    return HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")