import os
from typing import Iterator
from dotenv import load_dotenv
from agno.agent import Agent, RunResponseEvent  
from agno.models.ollama import Ollama
from agno.models.google import Gemini
from agno.utils.pprint import pprint_run_response

load_dotenv()

agent = Agent(  
    model=Ollama(id="cnmoro/gemma3-gaia-ptbr-4b:q4_k_m", provider="Ollama", host="http://localhost:11434"),  
    description="Você é um professor da área de TI com 20 anos experiência.",  
    markdown=True  
)

'''
agent = Agent(  
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),  
    description="Você é um professor da área de TI com 20 anos experiência.",  
    markdown=True  
)
''' 

response: Iterator[RunResponseEvent] = agent.run("Explique um LLM de forma didática.", stream=True)
pprint_run_response(response, markdown=True)
