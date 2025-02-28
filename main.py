#!/usr/bin/env python3
import argparse
from devflow_manager import DevFlowManager
from utils.logger import setup_logger

def parse_arguments():
    """
    Parses command-line arguments required to run the DevAutomator.
    """
    parser = argparse.ArgumentParser(
        description="DevAutomator: An AI-powered automated development process."
    )
    parser.add_argument("--api-key", required=True, help="Your OpenAI API key")
    parser.add_argument("--llm-backend", default="o1-mini", help="LLM backend to use (e.g., o1-mini, gpt-4)")
    parser.add_argument("--research-topic", default="YOUR DEVELOPING IDEA", help="Your developing project idea")
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    # Setup shared configuration for the entire workflow
    config = {
        "openai_api_key": args.api_key,
        "llm_backend": args.llm_backend,
        "research_topic": args.research_topic,
        # Predefined task notes to guide planning and overall flow
        "task_notes": [
            "Setup development environment",
            "Implement core features",
            "Write unit tests",
            "Prepare deployment scripts"
        ],
        "build_options": "Default build options",
        "test_options": "Default test options",
        "deployment_options": "Default deployment options",
        "documentation_options": "Default documentation options"
    }
    
    # Initialize logger for the main module
    logger = setup_logger("main")
    logger.info("Starting DevAutomator...")
    
    # Instantiate the development flow manager with the configuration
    manager = DevFlowManager(config)
    
    # Run the complete development automation flow
    success = manager.run_development_flow()
    
    if success:
        logger.info("Development flow completed successfully.")
    else:
        logger.error("Development flow encountered errors.")

if __name__ == "__main__":
    main()
