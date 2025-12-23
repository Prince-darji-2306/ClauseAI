import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.llms.groq import Groq
from engines.query_engine import query_routing

load_dotenv()

@st.cache_resource
def get_llm():
    return Groq(model='meta-llama/llama-4-scout-17b-16e-instruct', 
               api_key = os.getenv('GROQ'))

def get_context(engines, selected, query, files):
    context = ''
    for i in selected:
        ans = engines[i-1].query(query).response
        context += f'''contract name : {files[i-1]} \n
                        context : {ans} \n \n '''
    return context

def Answer(engines, query, files):
    llm = get_llm()
    
    ans = query_routing(llm, query, len(engines))

    context = get_context(engines, ans[0], ans[1], files)
    memory = st.session_state.memory
     
    final_prompt = f"""
        User query:
        {query}

        Summarized Memory : 
        {memory.get()}

        Answer based on the following document context and Previous memory:
        {context}
        """

    return llm.stream_complete(final_prompt)