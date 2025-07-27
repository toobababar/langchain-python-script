# LangChain Batch Processor

This is a python script powered by LangChain and OpenAI's gpt-4o-mini model that takes in JSONL files containing user prompts for LLM model. The script will automate batch processing of prompts, invoke the model and store the responses in new JSONL files after inferencing.

## Features

- Reads `.jsonl` prompt files from  `input_prompts/`
- Processes using OpenAI model via LangChain
- Saves structured responses to `output_responses/`
- Handles errors gracefully and generates logs
- LangSmith integrated for evaluation
- To reduce latency in case of large prompt files, `.jsonl` is used instead of 'json'

## Setup

```bash
    # Create virtual environment
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

    # Install requirements
    pip install -r requirements.txt

    # Run
    python prod/src/main.py





