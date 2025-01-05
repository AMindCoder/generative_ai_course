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

def few_shot_example():
    """
    Demonstrate few-shot prompting where the model performs a task with a few examples
    """
    user_prompt = "Here are some examples:\nFeedback: 'The item arrived damaged' -> Category: Product Quality\nFeedback: 'Shipping took too long' -> Category: Delivery\nFeedback: 'Great customer support' -> Category: Service\n\nNow classify this feedback: 'The representative was very rude on the phone'"
    system_prompt = "You are a helpful assistant that classifies customer feedback into categories: Product Quality, Service, Delivery, Price"
    response = get_answer(system_prompt, user_prompt)
    print(response)

if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())
    zero_shot_example()
