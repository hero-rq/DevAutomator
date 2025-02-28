import argparse
import logging
from openai import OpenAI
from devflow_manager import DevFlowManager

def parse_arguments():
    """Parses command-line arguments required to run DevAutomator."""
    parser = argparse.ArgumentParser(
        description="DevAutomator: An AI-powered automated development process."
    )
    parser.add_argument("--api-key", required=True, help="Your OpenAI API key")
    parser.add_argument(
        "--llm-backend",
        choices=["gpt-4o", "gpt-4", "gpt-3.5-turbo", "o1-mini"],
        default="gpt-4o",
        help="Choose an LLM backend"
    )
    parser.add_argument("--research-topic", default="YOUR DEVELOPING IDEA", help="Your developing project idea")
    return parser.parse_args()

def generate_code(api_key, research_topic):
    """
    Uses the OpenAI API to generate a Python script based on the given research topic and task notes.
    """
    # Construct the prompt for code generation
    prompt = (
        f"Generate a complete Python script that fulfills the following requirements:\n"
        f"Research Topic: {research_topic}\n"
        "Ensure the code is well-commented and structured for a development automation process."
    )
    
    # Set the API key
    OpenAI.api_key = api_key

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            n=1,
            stop=None,
        )
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

    code = response.choices[0].text.strip()
    return code

def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Setup shared configuration
    config = {
        "openai_api_key": args.api_key,
        "llm_backend": args.llm_backend,
        "research_topic": args.research_topic,
    }

    generated_code = generate_code(args.api_key, args.research_topic)
    
    if generated_code:
        print("=== Generated Code ===")
        print(generated_code)
    else:
        print("Failed to generate code.")

if __name__ == "__main__":
    main()
