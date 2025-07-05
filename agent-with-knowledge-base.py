import os
from typing import Iterator
from agno.agent import Agent, RunResponseEvent
from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.embedder.google import GeminiEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.utils.pprint import pprint_run_response

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
    description="Você é um expert em Docker",
    instructions=[
        "Busque por informações sobre o funcionamento da tecnologia Docker na sua base de conhecimento.",
        "Se a pergunta for mais adequada para a web, faça uma pesquisa na web para preencher as lacunas.",
        "Prefira as informações da sua base de conhecimento aos resultados da web."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["http://files.cod3r.com.br/apostila-docker.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="docker",
            search_type=SearchType.hybrid,
            embedder=GeminiEmbedder(id="gemini-embedding-exp-03-07", api_key=os.getenv("GEMINI_API_KEY")),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

if agent.knowledge is not None:
    agent.knowledge.load()

response: Iterator[RunResponseEvent] = agent.run("Como posso buildar uma imagem local?", stream=True)
pprint_run_response(response, markdown=True)
