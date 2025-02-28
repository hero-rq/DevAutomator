import logging
from openai import OpenAI  # OpenAI v1.x client
from utils.logger import setup_logger  # Centralized logger from utils

class DocumentationAgent:
    def __init__(self, config):
        """
        Initializes the DocumentationAgent with the given configuration.
        :param config: A configuration object/dictionary containing documentation settings.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("DocumentationAgent initialized with configuration.")
        # Initialize OpenAI Client
        self.client = OpenAI(api_key=self.config.get("openai_api_key", ""))

    def build_documentation_prompt(self, project_summary, code_structure):
        """
        Constructs the prompt for generating comprehensive project documentation.
        :param project_summary: A string summary of the project.
        :param code_structure: A string representing the structure of the project code.
        :return: A formatted prompt string.
        """
        prompt = (
            f"Generate comprehensive documentation for a software project with the following details:\n"
            f"Project Summary: {project_summary}\n"
            f"Code Structure: {code_structure}\n\n"
            "The documentation should include:\n"
            "- An overview\n"
            "- Installation instructions\n"
            "- Usage examples\n"
            "- Contribution guidelines\n"
            "- Version control and update notes if applicable."
        )
        return prompt

    def generate_documentation(self, project_summary, code_structure):
        """
        Uses the OpenAI API to generate comprehensive project documentation.
        :param project_summary: A string summary of the project.
        :param code_structure: A string representing the structure of the project code.
        :return: Generated documentation text as a string.
        """
        try:
            self.logger.info("Querying OpenAI API for documentation generation...")
            prompt = self.build_documentation_prompt(project_summary, code_structure)
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert technical writer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300  # Adjust as needed for more detailed documentation
            )
            documentation = response.choices[0].message.content.strip()
            self.logger.info("Received documentation from OpenAI API.")
            return documentation
        except Exception as e:
            self.logger.error(f"OpenAI API call failed for documentation generation: {e}")
            return "Documentation generation failed."

    def update_documentation_file(self, documentation, filepath="README.md", append=False):
        """
        Writes the generated documentation to a file.
        :param documentation: The documentation text to write.
        :param filepath: Path to the documentation file.
        :param append: If True, append to the existing file instead of overwriting.
        :return: Boolean indicating whether the file update was successful.
        """
        try:
            mode = "a" if append else "w"
            action = "Appending to" if append else "Overwriting"
            self.logger.info(f"{action} documentation file at {filepath}...")
            with open(filepath, mode) as f:
                if append:
                    f.write("\n\n" + documentation)
                else:
                    f.write(documentation)
            self.logger.info("Documentation file updated successfully.")
            return True
        except Exception as e:
            self.logger.error(f"Failed to update documentation file: {e}")
            return False

    def generate_and_update_documentation(self, project_summary, code_structure, filepath="README.md", append=False):
        """
        Orchestrates the generation of documentation and updates the documentation file.
        :param project_summary: A string summary of the project.
        :param code_structure: A string representing the structure of the project code.
        :param filepath: Path to the documentation file.
        :param append: If True, append to the existing file instead of overwriting.
        :return: The generated documentation text.
        """
        self.logger.info("Starting full documentation generation and update process...")
        documentation = self.generate_documentation(project_summary, code_structure)
        update_success = self.update_documentation_file(documentation, filepath, append)
        if update_success:
            self.logger.info("Documentation process completed successfully.")
        else:
            self.logger.error("Documentation process encountered errors during file update.")
        return documentation

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",  # Replace with your actual API key
        "documentation_options": "Default documentation settings"
    }
    doc_agent = DocumentationAgent(sample_config)
    
    project_summary = (
        "DevAutomator is an AI-powered development workflow that integrates planning, building, testing, "
        "deployment, and documentation generation using intelligent agents."
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
    
    # Generate and update documentation in one step
    documentation = doc_agent.generate_and_update_documentation(project_summary, code_structure, filepath="README.md", append=True)
    print("Generated Documentation:\n", documentation)
