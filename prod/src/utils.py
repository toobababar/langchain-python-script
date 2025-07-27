import os
import logging
import getpass
import json
from pathlib import Path
from dotenv import load_dotenv

def setup_environment():
    """Load environment variables from .env file."""
    try:
        load_dotenv()
    except ImportError:
        logging.warning("Could not load .env file. Ensure python-dotenv is installed.")
    
    os.environ["LANGSMITH_TRACING"] = "true"

    if "LANGSMITH_API_KEY" not in os.environ:
        os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")

    if "LANGSMITH_PROJECT" not in os.environ:
        project_name = getpass.getpass("Enter your LangSmith project name: ")
        os.environ["LANGSMITH_PROJECT"] = project_name or "default"
    
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

    logging.info("Environment setup complete.")

def read_prompts_from_jsonl(file_path: Path) -> list:
    """Reads prompt strings from JSONL file."""
    prompts = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    prompt = obj.get("prompt")
                    if prompt:
                        prompts.append(prompt)
                except json.JSONDecodeError as e:
                    logging.warning(f"Could not decode JSON from line in {file_path}: {e}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    return prompts

def write_results_to_jsonl(output_path: Path, results: list):
    """Write a list of results to a JSONL file."""
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
