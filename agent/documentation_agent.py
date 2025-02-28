import logging
import openai
from utils.logger import setup_logger  # Centralized logger from utils

class DocumentationAgent:
    def __init__(self, config):
        """
        Initializes the Documentation Agent with the given configuration.
        :param config: A configuration object/dictionary containing documentation settings.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("DocumentationAgent initialized with configuration.")
        # Set up the OpenAI API key from configuration if provided.
        openai.api_key = self.config.get("openai_api_key", "")

    def generate_documentation(self, project_summary, code_structure):
        """
        Uses the OpenAI API to generate comprehensive project documentation.
        :param project_summary: A string summary of the project.
        :param code_structure: A string representing the structure of the project code.
        :return: Generated documentation text as a string.
        """
        try:
            self.logger.info("Querying OpenAI API for documentation generation...")
            prompt = (
                f"Generate comprehensive documentation for a software project with the following details:\n"
                f"Project Summary: {project_summary}\n"
                f"Code Structure: {code_structure}\n"
                "The documentation should include an overview, installation instructions, usage examples, and contribution guidelines."
            )
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert technical writer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=250
            )
            documentation = response.choices[0].message.content.strip()
            self.logger.info("Received documentation from OpenAI API.")
            return documentation
        except Exception as e:
            self.logger.error(f"OpenAI API call failed for documentation generation: {e}")
            return "Documentation generation failed."

    def update_documentation_file(self, documentation, filepath="README.md"):
        """
        Writes the generated documentation to a file.
        :param documentation: The documentation text to write.
        :param filepath: Path to the documentation file.
        :return: Boolean indicating whether the file update was successful.
        """
        try:
            self.logger.info(f"Updating documentation file at {filepath}...")
            with open(filepath, "w") as f:
                f.write(documentation)
            self.logger.info("Documentation file updated successfully.")
            return True
        except Exception as e:
            self.logger.error(f"Failed to update documentation file: {e}")
            return False

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",  # Replace with your actual API key
        "documentation_options": "Default documentation settings"
    }
    doc_agent = DocumentationAgent(sample_config)
    project_summary = (
        "DevAutomator is an automated development workflow that integrates planning, building, testing, "
        "deployment, and documentation generation using AI-driven agents."
    )
    code_structure = """
DevAutomator/
├── main.py
├── config.py
├── devflow_manager.py
├── requirements.txt
├── setup.py
├── Makefile
├── Dockerfile
├── README.md
├── LICENSE
├── agents/
│   ├── planning_agent.py
│   ├── build_agent.py
│   ├── test_agent.py
│   ├── deployment_agent.py
│   └── documentation_agent.py
└── utils/
    ├── logger.py
    └── helper_functions.py
    """
    documentation = doc_agent.generate_documentation(project_summary, code_structure)
    print("Generated Documentation:\n", documentation)
    update_success = doc_agent.update_documentation_file(documentation)
    print("Documentation file update:", "Success" if update_success else "Failure")
