import time
import streamlit as st
from utils.memory import get_state
from engines.llm_engine import Answer
from doc_loader import load_uploaded_files
from llama_index.core.llms import ChatMessage

st.set_page_config(page_title='LegalGPT | Contract AI Assistant', layout='wide', page_icon='static/img/icon.png')
get_state()

with open("static/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.title('Navigation')
    if st.button('Upload pdf 📃'):
        st.session_state.page = 'upload'
    if st.button("Doc Q&A 😉"):
        st.session_state.page = 'chat'

if st.session_state.page == 'upload':
    st.title('Upload your Legal doc')
    files = st.file_uploader('Upload pdfs', type='pdf', accept_multiple_files=True)
    if files:
        with st.spinner('loading Files'):
            st.session_state.engine, st.session_state.files = load_uploaded_files(files)
            get_state(clear = True)

            st.success('Document loading and processing is done...')
            st.session_state.page = 'chat'
        time.sleep(0.5)
        st.rerun()
            
elif st.session_state.page == 'chat':
    engine = st.session_state.engine
    files = st.session_state.files
    
    if engine:
        st.title("Let's Discuss your Legal Terms ?")
        query = st.chat_input('Feel free to ask 😉')

        for msg in st.session_state.chat_history:
            if msg["type"] == "user":
                st.markdown(f'<div class="user-msg">{msg["text"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(msg["text"])

        if query and query.strip():

            st.session_state.chat_history.append({"type": "user", "text": query})
            st.session_state.memory.put(ChatMessage(role="user", content = query))
            st.markdown(f'<div class="user-msg">{query}</div>', unsafe_allow_html=True)
    
            llm_stream = Answer(engine, query, files)

            data = ''

            stream_placeholder = st.empty()
            for chunk in llm_stream:
                data += chunk.delta
                stream_placeholder.markdown(data, unsafe_allow_html=True)

            st.session_state.chat_history.append({"type": "assistant", "text": data})
            st.session_state.memory.put(ChatMessage(role="assistant", content = data))
    
    else:
        st.markdown('-----------------------------')
        st.error('First Upload the Documents')
