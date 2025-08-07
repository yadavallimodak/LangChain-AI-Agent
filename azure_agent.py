# azure_agent.py

import os

from dotenv import load_dotenv

from langchain_openai import AzureChatOpenAI



# Load environment variables from .env

load_dotenv()



def load_model():

    return AzureChatOpenAI(

        azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),

        azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME"),

        openai_api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),

        openai_api_key=os.environ.get("AZURE_OPENAI_API_KEY")

    )
