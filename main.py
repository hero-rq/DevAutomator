#!/usr/bin/env python3
import argparse
import logging
from openai import OpenAI
from devflow_manager import DevFlowManager

# Logger setup
def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    return logger

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

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    # Setup shared configuration
    config = {
        "openai_api_key": args.api_key,
        "llm_backend": args.llm_backend,
        "research_topic": args.research_topic,
        "task_notes": [
            "Setup development environment",
            "Implement core features",
            "Write unit tests",
            "Prepare deployment scripts"
        ],
    }
    
    # Initialize logger
    logger = setup_logger("main")
    logger.info("Starting DevAutomator...")

    # Initialize OpenAI Client
    client = OpenAI(api_key=args.api_key)

    # Instantiate the development flow manager with configuration
    manager = DevFlowManager(config, client)

    # Run the complete development automation flow
    success = manager.run_development_flow()

    if success:
        logger.info("Development flow completed successfully.")
    else:
        logger.error("Development flow encountered errors.")

if __name__ == "__main__":
    main()

