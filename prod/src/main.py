import logging
import time
from pathlib import Path
# Importing custom modules
from utils import setup_environment, read_prompts_from_jsonl, write_results_to_jsonl
from model_handler import get_model, run_prompt

# --- Configuration ---
# Define directories
INPUT_DIR = Path("input_prompts")
OUTPUT_DIR = Path("output_responses")

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s - %(message)s')

# --- Main Application Logic ---
def main():
    """Main function to run the batch processing script."""
    # Load .env variables and prompt for any missing API keys
    setup_environment()
    
# 1. Initialize model handler
try:
    model = get_model()
except EnvironmentError as e:
    logging.error(f"Model initialization failed: {e}")

# 2. Find input files
input_files = list(INPUT_DIR.glob("*.jsonl"))
if not input_files:
    logging.warning(f"No input JSONL files found in {INPUT_DIR}.")

logging.info(f"Found {len(input_files)} file(s) to process.")

# 3. Process each file
for file_path in input_files:
    logging.info(f"Processing file: {file_path.name}")
    prompts = read_prompts_from_jsonl(file_path)
    if not prompts:
        logging.warning(f"No prompts found in {file_path.name}. Skipping file.")
        continue
    
    results = []
    for prompt in prompts:
        try:
            response = run_prompt(model, prompt)
            results.append({"prompt": prompt, "response": response})
        except Exception as e:
            results.append({"prompt": prompt, "error": str(e)})

    # 4. Save the results
    output_file = OUTPUT_DIR / f"response_{file_path.stem}.csv"
    write_results_to_jsonl(output_file, results)
    logging.info(f"Successfully saved results to {output_file.name}")

logging.info(f"--- Batch processing complete at {time.ctime()} ---")

if __name__ == "__main__":
    main()
