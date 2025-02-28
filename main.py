import argparse
import logging
import os
from openai import OpenAI  # OpenAI v1.x client

def parse_arguments():
    """Parses command-line arguments required to run DevAutomator."""
    parser = argparse.ArgumentParser(
        description="DevAutomator: An AI-powered automated development process."
    )
    parser.add_argument("--api-key", help="Your OpenAI API key")
    parser.add_argument(
        "--llm-backend",
        choices=["gpt-4o", "gpt-3.5-turbo", "o1-mini"],
        default="gpt-4o",
        help="Choose an LLM backend: gpt-4o (rich multimodal), gpt-3.5-turbo (everyday chat), or o1-mini (advanced reasoning)"
    )
    parser.add_argument(
        "--research-topic",
        default="YOUR DEVELOPING IDEA",
        help="Your developing project idea"
    )
    return parser.parse_args()

def generate_code(api_key, research_topic, llm_backend):
    """
    Uses the OpenAI API to generate a Python script based on the given research topic.
    Supports chat-based models: gpt-4o, gpt-3.5-turbo, and o1-mini.
    """
    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=api_key)

    # Construct the prompt for code generation
    prompt = (
        f"Generate a complete Python script that fulfills the following requirements:\n"
        f"Research Topic: {research_topic}\n"
        "Ensure the code is well-commented and structured for a development automation process."
    )

    try:
        # Corrected API call: use chat.completions.create instead of ChatCompletion.create
        response = client.chat.completions.create(
            model=llm_backend,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.5,
            n=1,
        )
        code = response.choices[0].message["content"].strip()
        return code
    except Exception as e:
        logging.error(f"Error during API call: {e}")
        return None

def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Retrieve API key from argument or environment variable
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    if not api_key:
        logging.error("OpenAI API key is required. Provide it via --api-key argument or OPENAI_API_KEY environment variable.")
        return

    # Generate the code using the provided arguments
    generated_code = generate_code(api_key, args.research_topic, args.llm_backend)
    
    if generated_code:
        print("=== Generated Code ===")
        print(generated_code)
    else:
        print("Failed to generate code.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

