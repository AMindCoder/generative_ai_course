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

def chain_of_thought_example():
    """
    Demonstrate chain-of-thought prompting for complex reasoning tasks
    """
    user_prompt = """Let's solve this step by step:
            Problem: In a school, there are 200 students. 60% of them take math classes, 
            40% take science classes, and 25% take both math and science. 
            How many students don't take either math or science classes?"""
    system_prompt = "You are a helpful assistant that solves complex reasoning tasks step by step."
    
    response = get_answer(system_prompt, user_prompt)
    print(response)

if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(override=True)
    chain_of_thought_example()
