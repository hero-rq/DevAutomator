#!/usr/bin/env python3
import argparse
import openai
import os

def parse_arguments():
    """Parses command-line arguments required for code generation."""
    parser = argparse.ArgumentParser(
        description="DevAutomator: Generate development code using the OpenAI API."
    )
    parser.add_argument("--api-key", required=False, help="Your OpenAI API key")
    parser.add_argument(
        "--llm-backend",
        choices=["gpt-4", "gpt-3.5-turbo"],
        default="gpt-4",
        help="Choose an LLM backend"
    )
    parser.add_argument(
        "--research-topic", 
        default="YOUR DEVELOPING IDEA", 
        help="Your development project idea"
    )
    return parser.parse_args()

def generate_code(api_key, research_topic, task_notes):
    """
    Uses the OpenAI API to generate a Python script based on the given research topic and task notes.
    """
    # Construct the messages for the chat completion
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": (
            f"Generate a complete Python script that fulfills the following requirements:\n"
            f"Research Topic: {research_topic}\n"
            f"Tasks: {', '.join(task_notes)}\n\n"
            "Ensure the code is well-commented and structured for a development automation process."
        )}
    ]
    
    # Set the API key for authentication
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=1024,
            temperature=0.5,
            n=1,
            stop=None,
        )
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    code = response.choices[0].message['content'].strip()
    return code

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    # Determine the API key to use
    api_key = args.api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: No API key provided. Set the OPENAI_API_KEY environment variable or use the --api-key argument.")
        return
    
    # Define the task notes guiding the development process
    task_notes = [
        "Setup development environment",
        "Implement core features",
        "Write unit tests",
        "Prepare deployment scripts"
    ]
    
    # Generate code using OpenAI API
    generated_code = generate_code(api_key, args.research_topic, task_notes)
    
    if generated_code:
        print("=== Generated Code ===")
        print(generated_code)
    else:
        print("Failed to generate code.")

if __name__ == "__main__":
    main()
