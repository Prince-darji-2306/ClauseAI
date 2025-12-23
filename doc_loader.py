import os
import faiss
import tempfile
from utils.embeddings import load_model
from llama_index.core.schema import Document
from utils.doc_processor import clean_legal_text
from engines.query_engine import get_query_engine
from concurrent.futures import ThreadPoolExecutor
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core import VectorStoreIndex, StorageContext



def process_pdf(uploaded_file):
    """Process a single PDF file and return a vector index."""
    reader = PyMuPDFReader()
    
    # Save uploaded file to a temporary path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name
    
    raw_docs = reader.load_data(tmp_path)
    full_text = " ".join([doc.text for doc in raw_docs])   # join all at once

    cleaned_text = clean_legal_text(full_text)
    # key_info = analyze_contract(cleaned_text)

    filename = uploaded_file.name 

    clean_doc = Document(text=cleaned_text, metadata={'filename': filename})

    splitter = SentenceSplitter(chunk_size=500, chunk_overlap=80)
    nodes = splitter.get_nodes_from_documents([clean_doc])

    storage_context = StorageContext.from_defaults(
        vector_store=FaissVectorStore(faiss_index=faiss.IndexFlatL2(384))
    )

    index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=load_model())

    os.remove(tmp_path)

    return index, filename

def load_uploaded_files(uploaded_files):
    if not uploaded_files:
        raise ValueError("No files uploaded")

    # Process files (parallel for multiple)
    if len(uploaded_files) == 1:
        results = [process_pdf(uploaded_files[0])]
    else:
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(process_pdf, uploaded_files))

    return get_query_engine(results)
