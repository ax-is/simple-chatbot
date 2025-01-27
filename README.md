---

# ChatBot: AI-Powered Q&A with PDF Uploads

![Screenshot from 2024-05-17 08-42-03](https://github.com/user-attachments/assets/cee40e75-9957-4e71-8493-433a8cd9db89)

This is a powerful AI chatbot that leverages *LangChain* as the main framework for orchestrating conversational workflows, *chatOllama* for running models locally, the *Phi 2 model by Microsoft* (with 2.7 billion parameters), and *Cohere embeddings* stored in *ChromaDB* to deliver accurate and context-rich responses. The chatbot has a user-friendly interface built using *Streamlit*, allowing users to ask questions and upload PDFs for document-based query answering.

---

## Key Features
- **LangChain for Workflow Management**: LangChain serves as the backbone of the chatbot, managing conversational logic, integrating document loaders, and orchestrating retrieval workflows. It enables seamless chaining of model reasoning and document-based responses.  
- **Local Model Execution**: Powered by **chatOllama**, the model runs efficiently on your local machine, ensuring privacy and reduced latency.
- **Phi 2 Model by Microsoft**: The chatbot locally runs **Phi 2**, a cutting-edge model with 2.7 billion parameters, providing powerful natural language processing and accurate question answering.
- **Persistent Embeddings with ChromaDB**: **Cohere embeddings** are stored and persisted in *ChromaDB*, enabling fast and efficient vector searches for document retrieval and contextual understanding.
- **PDF Upload and Querying**: Users can upload PDFs, and the chatbot can extract, analyze, and answer questions based on the document content.
- **User-Friendly UI**: Built with **Streamlit**, offering an intuitive interface that allows users to interact easily with the chatbot and upload documents for processing.

---

## Technologies Used
- **LangChain**: The primary framework for structuring conversational workflows, integrating document processing, and managing seamless interactions between the model and embeddings.
- **chatOllama**: Used to run models locally.
- **Microsoft Phi 2 Model**: A state-of-the-art model with 2.7 billion parameters.
- **Cohere Embeddings**: Provides the embeddings for semantic search.
- **ChromaDB**: A vector database to store and persist embeddings.
- **Streamlit**: Used for building the front-end UI.

---

## How It Works
1. Users can interact with the chatbot through a simple question-answer interface or upload PDFs to query document-specific information.
2. The chatbot processes the user's query using **LangChain** to organize workflows, structure input-output pipelines, and integrate the **Phi 2 model** for reasoning.
3. If a PDF is uploaded, **LangChain’s document loaders** extract its content, generate embeddings using **Cohere**, and persist them in **ChromaDB**. The chatbot then retrieves and answers questions based on the document.

---

Let me know if you'd like further refinements! 🚀
## How It Works
1. Users can interact with the chatbot through a simple question-answer interface or upload PDFs to query document-specific information.
2. The chatbot processes the user's query using *Phi 2 model* and retrieves relevant information from the *Cohere embeddings* stored in *ChromaDB*.
3. If a PDF is uploaded, the bot processes it to generate embeddings and fetches the appropriate responses from the document.

## Screenshots
![Screenshot from 2024-09-09 03-11-20](https://github.com/user-attachments/assets/685f7914-573b-4bdb-b8ec-a1badbb15fb1)
![Screenshot from 2024-09-09 03-13-42](https://github.com/user-attachments/assets/4d69910b-3350-40ad-b20c-46fca19e882b)
![Screenshot from 2024-09-09 03-14-05](https://github.com/user-attachments/assets/4f708d9b-de3d-41cf-b6c1-dc4035870fc3)

---

## License

This project is licensed under the MIT License.
