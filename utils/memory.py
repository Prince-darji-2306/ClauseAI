import streamlit as st
from llama_index.core.memory import ChatMemoryBuffer

def get_state(clear = False):
    if clear:
        st.session_state.memory.reset()
        st.session_state.chat_history = []

    else:
        if not 'page' in st.session_state:
            st.session_state.page = 'upload'
        if not 'engine' in st.session_state:
            st.session_state.engine = None
        if not 'files' in st.session_state:
            st.session_state.files = None
        if not 'chat_history' in st.session_state:
            st.session_state.chat_history = []
        if not 'memory' in st.session_state:
            st.session_state.memory = ChatMemoryBuffer.from_defaults(
                    token_limit = 800
                )