import os
import uuid
from datetime import datetime

from anyio.lowlevel import checkpoint
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
import gradio as gr
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm = ChatOllama(model="gemma4")

search_tool = TavilySearchResults()
def get_date():
    """Get the current Date"""
    return datetime.now().strftime("%Y-%m-%d")

conn = sqlite3.connect("chatbot_memory.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)
system_prompt = """
You are a helpful assistant.
Answer all user queries
Use the get_date tool ONLY when the user is explicitly asking about  todays date
Use the search_tool to get the latest or up to date information
"""
agent = create_agent(
    model=llm,
    tools=[get_date,search_tool],
    system_prompt=system_prompt,
    checkpointer=checkpointer)
#user_query = input("Enter a query:")


def chat(message,history,thread_id):
    config = {"configurable":{"thread_id": thread_id}}
    response = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
                            config)
    last_response = response["messages"][-1].content
    return last_response


with gr.Blocks() as demo:
    gr.Markdown("# AI Chatbot")
    thread_id = gr.State(value=lambda: str(uuid.uuid4()))
    gr.ChatInterface(fn=chat, additional_inputs=[thread_id])

demo.launch()