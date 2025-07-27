from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
import os
import logging

def get_model():
    """ Initialize and return the chat model."""
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("FATAL: OPENAI_API_KEY not found in environment. Please set it in .env file.")
        raise EnvironmentError("OPENAI_API_KEY is required to initialize the model.")
    try:
        return init_chat_model("gpt-4o-mini", model_provider="openai")
    except Exception as e:
        logging.error(f"Failed to initialize model: {e}")
        raise RuntimeError("Model initialization failed. Check your API key and network connection.")

def run_prompt(model, prompt: str) -> str:
    """Run a prompt through the model and return the response."""
    messages = [
        SystemMessage(content="You are a helpful assistant. Answer the user queries in 3 sentences. Avoid giving details."),
        HumanMessage(content=prompt),
    ]
    try:
        response = model.invoke(messages)
        return response.content
    except Exception as e:
        logging.error(f"Error running prompt: {e}")
        raise RuntimeError(f"Failed to run prompt: {prompt}. Error: {e}")