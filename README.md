# Generative AI Course - Prompt Engineering Labs

This repository contains hands-on labs for learning prompt engineering techniques with Large Language Models (LLMs).


## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Azure OpenAI credentials:
```
AZURE_OPENAI_API_KEY=your_endpoint_url
AZURE_OPENAI_ENDPOINT=your_api_key

```

## Weekly Labs

### Week 1: Basic Prompting Techniques
- Zero-shot prompting: Learn how to craft prompts without examples

### Week 2: Advanced Prompting
- Few-shot prompting: Using examples to guide the model's responses

### Week 3: Complex Reasoning
- Chain of thought prompting: Breaking down complex problems into steps

## Running the Labs

Each lab can be run independently:
```bash
python week1_basics/zero_shot_prompting.py
```
