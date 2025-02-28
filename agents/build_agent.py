import logging
from utils.logger import setup_logger  # Centralized logger from utils
from openai import OpenAI  # OpenAI v1.x client

class BuildAgent:
    def __init__(self, config):
        """
        Initializes the BuildAgent with the given configuration.
        :param config: A configuration object/dictionary containing build options.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("BuildAgent initialized with configuration.")

        # Initialize OpenAI Client
        self.client = OpenAI(api_key=self.config.get("openai_api_key", ""))

    def compile_code(self):
        """
        Generates a complete and optimized Python build script using the OpenAI API.
        :return: Generated code as a string.
        """
        self.logger.info("Starting build code generation...")

        # Construct a prompt for generating a build script
        prompt = (
            "Generate a complete and optimized Python build script that performs the following tasks:\n"
            "- Cleans previous builds\n"
            "- Compiles source code\n"
            "- Links libraries\n"
            "- Generates binaries\n\n"
            "Include detailed comments for clarity."
        )

        code_output = self.get_code_output(prompt)
        self.logger.info("Build code generation completed.")
        return code_output

    def get_code_output(self, prompt):
        """
        Uses the OpenAI API to generate code output based on the given prompt.
        :param prompt: A string prompt to send to the OpenAI API.
        :return: The generated code as a string.
        """
        try:
            self.logger.info("Querying OpenAI API for code generation...")
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert in build automation and Python scripting."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,  # Adjust token limit as needed
            )
            generated_code = response.choices[0].message.content.strip()
            self.logger.info("Received code from OpenAI API.")
            return generated_code
        except Exception as e:
            self.logger.error(f"OpenAI API call failed: {e}")
            return "No code generated."

    def run_build(self):
        """
        Executes the build code generation process.
        :return: The generated build script as a string.
        """
        self.logger.info("Running the build code generation process...")
        code = self.compile_code()
        return code

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "build_options": "Default options",
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE"  # Replace with your actual API key
    }
    build_agent = BuildAgent(sample_config)
    generated_code = build_agent.run_build()
    print("=== Generated Build Code ===")
    print(generated_code)
