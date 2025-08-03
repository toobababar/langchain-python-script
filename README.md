# LangChain Batch Prompt Processor for Instruction Fine-Tuning

This is a Python-based automation script powered by **LangChain** and **OpenAI's GPT-4o-mini** model. The script processes batches of input prompts to generate high-quality LLM outputs ideal for creating datasets used in **instruction fine-tuning** for other models.

## Project Overview

This tool automates the process of **inference across multiple prompts**, taking input prompt files (`.jsonl` format) and returning structured responses in the comma seperated value format. These output files contain both the original prompt and its corresponding LLM-generated response making them perfect candidates for supervised fine-tuning or instruction-tuning pipelines.

## Key Features

- **Batch Processing of Prompts** using LangChain’s powerful abstractions.
- Uses **OpenAI GPT-4o-mini** for fast and efficient inferencing.
- **Output-ready `.csv` format** for model training pipelines.
- Automates prompt response pairing for massive input datasets.
- Fully configurable via `.env` and supports `LangSmith` tracing for evaluation.

## Input Format

Input files must be in `.jsonl` (JSON Lines) format with one prompt per line:

```json
{"prompt": "What is the capital of France?"}
{"prompt": "Summarize the benefits of solar energy."}
```
## Output Format

For each prompt, the model returns a structured output:

```csv
prompt,response,error
"What is the capital of France?","The capital of France is Paris.",""
"Summarize the benefits of solar energy.","Solar energy is renewable, clean, and reduces electricity costs.",""
```
**prompt:** The original input prompt.\n
**response:** The model’s output.\n
**error:** Any error message (if the model failed to return a response).

## Setup Instructions

### 1. Clone the repo:

```bash
git clone https://github.com/toobababar/langchain-python-script.git
cd langchain-python-script
```
### 2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
### 3. Install dependencies:

```bash
pip install -r requirements.txt
```
### 4. Configure API keys:

Create a .env file and add:
```bash
OPENAI_API_KEY=your-openai-key
LANGSMITH_API_KEY=your-langsmith-key
LANGSMITH_PROJECT=your-project-name
```
### 5. Add your prompt files to input_prompts/

### 6. Run the script:

```bash
python src/main.py
```
## Why .jsonl?

**Using .jsonl (one JSON object per line) instead of .json avoids memory bottlenecks when working with large prompt sets. It enables:**
- Efficient line-by-line streaming
- Reduced compute overhead
- Easier debugging and resumption in case of errors

## Use Case

**This script is ideal for:**
- Creating custom instruction datasets
- Bootstrapping fine-tuning data from existing prompts
- Evaluating LLM behavior on real-world inputs
- Training distilled or local models using OpenAI-generated outputs

## License

This project is licensed under the MIT License.















