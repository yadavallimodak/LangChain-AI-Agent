# agent.py



'''



Modakapriya Yadavalli

Agentic Pattern Recommender

Date: 07/28/2025



'''



import os

import tempfile

from dotenv import load_dotenv

import gradio as gr

from tools.patternrecommender import FlowRecommender

import random

from tools.toolplanning import run_tool_agent

from rag import encode_file, retrieve_context_per_question



load_dotenv()



bot_message = random.choice([

    "Hello there, welcome to AWR!",

    "Greetings, welcome to AWR.",

    "Hi! A great day to ask your questions on AWR."

])



intro_text = """

Welcome to the Agentic AI Assistant



This assistant helps you identify the best agentic workflow pattern

(such as Prompt Chaining, Routing, Reflection, Parallelization, etc.)

based on your request.



In addition, it supports **Retrieval-Augmented Generation (RAG)**:  

you can upload a PDF or TXT file, and the assistant will retrieve

relevant sections from the document to answer your questions with context.



Example Prompt



"Which agentic workflow pattern would be most effective if I want

to analyze a document, extract key insights, and then summarize them

for different teams?"



Or try uploading a PDF and asking:

"Summarize the key points from this file in simple terms."

"""



recommender = FlowRecommender()



def classify_workflow(message, history, uploaded_file):

    message_lower = message.lower()

    rag_keywords = ["summarize", "analyze", "explain", "context"]



    if uploaded_file is not None and any(kw in message_lower for kw in rag_keywords):

        tmp_path = uploaded_file.name



        try:

            vs = encode_file(tmp_path)

            retriever = vs.as_retriever(search_kwargs={"k": 3})

            context = retrieve_context_per_question(message, retriever)

            from azure_agent import load_model

            llm = load_model()

            response = llm.invoke(f"Summarize the following content:\n\n{context}")

            return response.content if hasattr(response, 'content') else str(response)

        except Exception as e:

            return f"RAG failed: {str(e)}"



    elif any(keyword in message_lower for keyword in ["search", "find", "look up", "latest", "internet", "recent", "trending"]):

        return run_tool_agent(message)



    else:

        return recommender.run(message)



def main():



    with open("theme.css", "r") as f:

        custom_css = f.read()

   

    with gr.Blocks(css=custom_css) as intro_block:

        with gr.Tab("Introduction"):

            gr.Markdown(intro_text)



    chatbot_component = gr.Chatbot(

        value=[{"role": "assistant", "content": f"""{bot_message}



                Welcome to the Agentic AI Assistant



                This assistant helps you identify the best agentic workflow pattern

                (such as Prompt Chaining, Routing, Reflection, Parallelization, etc.)

                based on your request.



                In addition, it supports Retrieval-Augmented Generation (RAG):  

                you can upload a PDF or TXT file, and the assistant will retrieve

                relevant sections from the document to answer your questions with context.



                Example Prompt



                "Which agentic workflow pattern would be most effective if I want

                to analyze a document, extract key insights, and then summarize them

                for different teams?"



                Or try uploading a PDF and asking:

                "Summarize the key points from this file in simple terms."

                """

            }],

        label="Agent Chatbot",

        autoscroll=True,

        type="messages",

        elem_id="chatbot",

        container=True

    )

    send_btn = gr.Button("Send")



    gr.HTML(

        """

        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

        """

    )



    gr.HTML(

        """

        <script>

        // Wait a little after each update to render Mermaid

        setInterval(() => {

            document.querySelectorAll("div.mermaid").forEach((el) => {

            if (!el.classList.contains("rendered")) {

                mermaid.init(undefined, el);

                el.classList.add("rendered");

            }

            });

        }, 500);

        </script>

        """

    )

   



    files_upload = gr.File(file_types = [".txt", ".pdf", ".doc"], label="Upload your file", file_count="single")



    gr.ChatInterface(

        fn=classify_workflow,

        title="KPMG Agentic Workflow Recommender (AWR)",

        chatbot = chatbot_component,

        textbox=gr.Textbox(placeholder="Describe your AI use case...", label="Your Request"),

        additional_inputs=[files_upload],

        css = custom_css

        # theme="soft"

    ).launch()

   



if __name__ == "__main__":

   

    main()

