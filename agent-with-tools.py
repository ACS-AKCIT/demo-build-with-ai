import os
from typing import Iterator
from dotenv import load_dotenv
from agno.agent import Agent, RunResponseEvent
from agno.models.google import Gemini
from agno.utils.pprint import pprint_run_response
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

agent = Agent(  
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),  
    description="Você é um especialista em IA Generativa para negócios.", 
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

response: Iterator[RunResponseEvent] = agent.run("Quais são os melhores nichos para empreender com IA?", stream=True)
pprint_run_response(response, markdown=True)
