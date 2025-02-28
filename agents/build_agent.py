import logging
from utils.logger import setup_logger  # Centralized logger from utils
from openai import OpenAI  # OpenAI v1.x client

class BuildAgent:
    def __init__(self, config):
        """
        Initializes the Build Agent with the given configuration.
        :param config: A configuration object/dictionary containing build options.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("BuildAgent initialized with configuration.")

        # Initialize OpenAI Client
        self.client = OpenAI(api_key=self.config.get("openai_api_key", ""))

    def compile_code(self):
        """
        Simulates the code compilation/building process.
        Optionally uses the OpenAI API to generate suggestions or code snippets.
        :return: Boolean indicating whether the build was successful.
        """
        self.logger.info("Starting build process...")

        # Simulated build steps
        steps = [
            "Cleaning previous builds",
            "Compiling source code",
            "Linking libraries",
            "Generating binaries"
        ]
        for step in steps:
            self.logger.info(f"{step}...")

        # Use OpenAI API to get build optimization suggestions
        suggestion = self.get_build_suggestion("How can I optimize the build process for faster compilation?")
        self.logger.info(f"Build optimization suggestion: {suggestion}")

        build_success = True  # Simulated build success
        self.logger.info("Build process completed successfully." if build_success else "Build process failed.")
        return build_success

    def get_build_suggestion(self, prompt):
        """
        Uses OpenAI API to get suggestions for build optimizations.
        :param prompt: A string prompt to send to OpenAI API.
        :return: The response from the API as a string.
        """
        try:
            self.logger.info("Querying OpenAI API for build suggestions...")
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert in build optimization."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=50
            )
            suggestion = response.choices[0].message.content.strip()
            self.logger.info("Received suggestion from OpenAI API.")
            return suggestion
        except Exception as e:
            self.logger.error(f"OpenAI API call failed: {e}")
            return "No suggestion available."

    def run_build(self):
        """
        Executes the full build process.
        :return: Result of the build (True if successful, False otherwise).
        """
        self.logger.info("Running the complete build process...")
        result = self.compile_code()
        return result

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "build_options": "Default options",
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE"  # Replace with your actual API key
    }
    build_agent = BuildAgent(sample_config)
    build_result = build_agent.run_build()
    print("Build result:", "Success" if build_result else "Failure")
