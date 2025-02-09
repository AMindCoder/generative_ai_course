# Import required modules
import os
import sys
from pathlib import Path

# Add the project root to Python path
current_dir = Path(__file__).resolve().parent
project_root = str(current_dir.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.azure_llm import get_answer

def zero_shot_example():
    """
    Demonstrate zero-shot prompting where the model performs a task without any examples
    """
    user_prompt = "Classify the sentiment of this text: 'I absolutely love this new phone!'"
    system_prompt = "You are a helpful assistant that classifies text into positive, negative, or neutral sentiment."
    response = get_answer(system_prompt, user_prompt)
    print(response)

if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(override=True)
    zero_shot_example()
