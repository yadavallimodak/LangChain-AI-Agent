Agentic Workflow Recommender (AWR)



Working website - https://nprd-pr-agent-pattern-recommender.azurewebsites.net/



The Agentic Workflow Recommender (AWR) is an interactive assistant that helps you figure out the most effective workflow pattern for your request. Whether the task involves analyzing documents, retrieving the latest insights, or coordinating multiple steps, the assistant recommends a structured approach to get it done.



The system is built using LangChain, Azure OpenAI, and Gradio, with support for Retrieval-Augmented Generation (RAG) so you can upload files and get context-aware responses.



1. What it Can Do:

   

🔹 Recommend Agentic Workflow Patterns



The assistant classifies your request into one of the following patterns, depending on complexity and needs:



- Prompt Chaining

- Routing / Handoff

- Reflection

- Parallelization

- Tool Use

- Planning (Orchestrator–Workers)

- Multi-Agent Pattern



🔹 Work with Uploaded Documents



- You can upload a PDF or TXT file and ask questions like:

- “Summarize this document for me.”

- “Explain the key points in simple terms.”



Behind the scenes, the system uses RAG to pull out relevant context and respond directly in the chat.



🔹 Simulate Search for Fresh Information



If your request requires the latest information (e.g., “What are the newest AI trends in audit?”), the assistant can perform a simulated search and provide up-to-date insights (still need to integrate it to working external search APIs - update as of July 20, 2025)



🔹 Interactive and Visual Chat Interface



- Built on Gradio, with a responsive chatbot layout

- Supports file uploads, scrolling chat history, and Mermaid.js diagrams to illustrate workflows

- Custom styling provided via theme.css



2. Tech Stack used



- Frontend: Gradio

- Backend: Python

- Models: Azure OpenAI (GPT-4o-mini)

- Frameworks & Tools: LangChain, FAISS (vector storage), Mermaid.js



Deployment: Docker + Azure Web Apps
