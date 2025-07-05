import os
from typing import Iterator
from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.agent import Agent, RunResponseEvent
from agno.models.perplexity import Perplexity
from agno.tools.yfinance import YFinanceTools
from agno.utils.pprint import pprint_run_response
from agno.tools.googlesearch import GoogleSearchTools

load_dotenv()

web_agent = Agent(
    name="Agente de busca na web",
    role="Busca por informações complementares na internet",
    model=Perplexity(id="sonar-pro", api_key=os.getenv("PERPLEXITY_API_KEY")),
    instructions="Sempre inclua as fontes",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Agente financeiro",
    role="Busca por dados financeiros",
    model=Gemini(id="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY")),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tabelas para mostrar os dados",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Gemini(id="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY")),
    instructions=["Use o Agente de busca na web para obter notícias atualizadas", "Use o Agente financeiro para obter dados financeiros de empresas"],
    show_tool_calls=True,
    markdown=True,
)

response: Iterator[RunResponseEvent] = agent_team.run("Retorne as últimas notícias e o desempenho financeiro das empresas Nvidia e Intel", stream=True)
pprint_run_response(response, markdown=True)
