# Generative AI Course - Prompt Engineering Labs

This repository contains hands-on labs for learning prompt engineering techniques with Large Language Models (LLMs).

## Project Structure

```
generative_ai_course/
├── config.py                # Azure OpenAI configuration and utilities
├── requirements.txt         # Project dependencies
├── week1_basics/           # Introduction to basic prompting
│   └── zero_shot_prompting.py
├── week2_advanced/         # Advanced prompting techniques
│   └── few_shot_prompting.py
└── week3_advanced/         # Complex reasoning and chain of thought
    └── chain_of_thought.py
```

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
ENDPOINT_URL=your_endpoint_url
DEPLOYMENT_NAME=your_deployment_name
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
