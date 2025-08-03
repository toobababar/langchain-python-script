import os
import logging
import getpass
import json
import csv
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

def write_results_to_csv(output_path: Path, results: list):
    """Write a list of results to a CSV file."""
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() == ".csv":
        fieldnames = ["prompt", "response", "error"]
        with output_path.open("w", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in results:
                writer.writerow({
                    "prompt": row.get("prompt", ""),
                    "response": row.get("response", ""),
                    "error": row.get("error", "")
                })
    else:
        raise ValueError(f"Unsupported file format: {output_path.suffix}")
