from langchain_ollama import ChatOllama
from config import OLLAMA_MODEL

# Initialize the LLM
llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0.2
)


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns the response.
    """
    response = llm.invoke(prompt)
    return response.content