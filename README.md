### GitHub README for the ChatBot Project

---

# ChatBot: AI-Powered Q&A with PDF Uploads

This is a powerful AI chatbot that leverages *Ollama API* for running models locally, *Phi 2 model by Microsoft* (with 2.7 billion parameters), and *Cohere embeddings* stored in *ChromaDB* to deliver accurate and context-rich responses. The chatbot has a user-friendly interface built using *Streamlit*, allowing users to ask questions and upload PDFs for document-based query answering.

## Key Features
- *Local Model Execution: Powered by **Ollama API*, the model runs efficiently on your local machine, ensuring privacy and reduced latency.
- *Phi 2 Model by Microsoft: The chatbot locally runs **Phi 2*, a cutting-edge model with 2.7 billion parameters, providing powerful natural language processing and accurate question answering.
- *Persistent Embeddings with ChromaDB: **Cohere embeddings* are stored and persisted in *ChromaDB*, enabling fast and efficient vector searches for document retrieval and contextual understanding.
- *PDF Upload and Querying*: Users can upload PDFs, and the chatbot can extract, analyze, and answer questions based on the document content.
- *User-Friendly UI: Built with **Streamlit*, offering an intuitive interface that allows users to interact easily with the chatbot and upload documents for processing.

## Technologies Used
- *Ollama API*: Used to run models locally.
- *Microsoft Phi 2 Model*: A state-of-the-art model with 2.7 billion parameters.
- *Cohere Embeddings*: Provides the embeddings for semantic search.
- *ChromaDB*: A vector database to store and persist embeddings.
- *Streamlit*: Used for building the front-end UI.

## How It Works
1. Users can interact with the chatbot through a simple question-answer interface or upload PDFs to query document-specific information.
2. The chatbot processes the user's query using *Phi 2 model* and retrieves relevant information from the *Cohere embeddings* stored in *ChromaDB*.
3. If a PDF is uploaded, the bot processes it to generate embeddings and fetches the appropriate responses from the document.

## Installation
1. Clone the repository:
    bash
    git clone https://github.com/your-username/chatbot-project.git
    
2. Install dependencies:
    bash
    pip install -r requirements.txt
    
3. Set up the required API keys for *Ollama, **Cohere, and **ChromaDB*.
4. Run the Streamlit app:
    bash
    streamlit run app.py
    

## Contributions
Feel free to open issues or pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### GitHub Repository Description

A powerful AI chatbot that uses Ollama API (local model execution), Microsoft Phi 2 model (2.7 billion parameters), and Cohere embeddings stored in ChromaDB. Features include answering user queries and allowing PDF uploads for document-based questions. Powered by a Streamlit UI for an easy-to-use interface.
