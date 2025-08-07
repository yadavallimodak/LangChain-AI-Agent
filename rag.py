# rag.py



import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, TextLoader

from langchain_community.vectorstores import FAISS

from langchain.text_splitter import RecursiveCharacterTextSplitter



from helper_functions import (

    EmbeddingProvider,

    get_langchain_embedding_provider,

    replace_t_with_space,

    retrieve_context_per_question,

    show_context

)



# Load environment variables

load_dotenv()



def encode_file(path, chunk_size=1000, chunk_overlap=200):

    """Loads a document (PDF or TXT), chunks it, embeds it, and stores it in FAISS."""



    # Step 1: Load

    if path.endswith(".pdf"):

        loader = PyPDFLoader(path)

    elif path.endswith(".txt"):

        loader = TextLoader(path)

    else:

        raise ValueError("Unsupported file type")



    docs = loader.load()



    # Step 2: Chunk

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=chunk_size,

        chunk_overlap=chunk_overlap,

        length_function=len

    )

    chunks = splitter.split_documents(docs)



    # Step 3: Clean & Embed

    cleaned_chunks = replace_t_with_space(chunks)

    embeddings = get_langchain_embedding_provider(EmbeddingProvider.OPENAI)  # Uses Azure config under the hood



    # Step 4: Build Vectorstore

    vectorstore = FAISS.from_documents(cleaned_chunks, embeddings)

    return vectorstore

