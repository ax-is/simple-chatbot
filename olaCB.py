import streamlit as st
from pdfminer.high_level import extract_text
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama
import time
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
import chromadb

#callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Initialize the Ollama model
llm = ChatOllama(model="phi")

# Initialize variables to store context and history
context = ""
source_texts = []
conversation_history = []
answer = ""  # Initialize answer variable

# Function to process PDF and generate response
def process_pdf_and_generate_response(pdf_file, message_content):
    global context, source_texts
    # Extract text from the uploaded PDF file
    text = extract_text(pdf_file)
    print("Text extracted...")
    # Write the extracted text to a temporary file
    with open('output_1.txt','w') as f:
        f.write(text)
    
    # Load and process the extracted text from PDF
    loader = TextLoader('output_1.txt', encoding='utf-8')
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    docs = text_splitter.split_documents(docs)
    print("Text split...")

    # Generate embeddings and create a vector store
    embeddings = CohereEmbeddings(cohere_api_key='2xGSkIkMc5b6XtimxY7cICQOwwv4aFQ0G00cvKfQ')

    
    vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
    client = chromadb.PersistentClient(path="/home/axis/Desktop/chatbot/chroma")
    print("Vector store created...")

    # Search for similar content based on user query
    output = vectorstore.similarity_search(query=message_content, k=5)
    print("Similarity search done...")
    
    # Concatenate found contents for context
    context = "\n".join([result.page_content for result in output])
    print(context)
    
    # Store the source texts for potential future use
    source_texts = [result.page_content for result in output]

    # Setup the template for generating responses
    message = "Context:" + context + "\nQuestion:" + message_content + "\nAnswer:"
    print(message)

    start = time.time()
    # Generate answer based on context and user query
    answer = llm.predict(message)
    end = time.time()
    print("Time taken -> ", end - start)
    return answer, source_texts

# Streamlit interface
st.set_page_config(page_title="ChatBot", page_icon="🤖")
st.title("ChatBot")


# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file (optional)", type="pdf")
#sources checkbox
display_source = st.checkbox("Display Sources")

# Text input for user message
with st.form(key='user_input_form'):
    message_content = st.text_input("Enter Query:")
    submitted = st.form_submit_button("Generate")

    if submitted:
        # If uploaded file is not None, process PDF and generate response
        if uploaded_file is not None:
            # Show loading spinner
            with st.spinner(""):
                answer, source_texts = process_pdf_and_generate_response(uploaded_file, message_content)
                prompt = PromptTemplate.from_template(message_content)
                chain = prompt | llm 
                st.write_stream(chain.stream({}))
        # Otherwise, generate answer directly
        else:
            # Show loading spinner
            with st.spinner(""):
                prompt = PromptTemplate.from_template(message_content)
                print(prompt)
                chain = prompt | llm 
                st.write_stream(chain.stream({}))
        
        # Display AI response
        # st.write_stream("**Phi_2:**", answer)
        # Display source texts if checkbox is checked
        if display_source:
            st.subheader("Source Texts:")
            for source_text in source_texts:
                st.write_stream(source_text)