from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

# Set user agent for web requests
os.environ['USER_AGENT'] = "your-user-agent-string"

def setup_rag(papers):
    # Initialize Ollama
    llm = Ollama(model="llama3.2")

    # Create a text splitter
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    
    # Split the papers into chunks
    texts = []
    for paper in papers:
        texts.extend(text_splitter.split_text(paper['abstract']))
    
    # Create embeddings
    embeddings = HuggingFaceEmbeddings()
    
    # Create a vector store
    db = FAISS.from_texts(texts, embeddings)
    
    # Create a prompt template
    prompt_template = """
    You are a research assistant. Given the following context and a question, provide a brief and informative answer.

    Context: {context}

    Question: {question}

    Answer:"""
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    # Create an LLM chain
    chain = prompt | llm
    
    return db, chain

def get_paper_description(db, chain, paper):
    question = f"Provide a brief description of the paper titled '{paper['title']}' based on its abstract."
    docs = db.similarity_search(question, k=4)
    context = " ".join([doc.page_content for doc in docs])
    input_data = {"context": context, "question": question}
    response = chain.invoke(input_data)
    return response.strip()