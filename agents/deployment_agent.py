import logging
from utils.logger import setup_logger  # Centralized logger from utils
from openai import OpenAI  # OpenAI v1.x client

class DeploymentAgent:
    def __init__(self, config):
        """
        Initializes the DeploymentAgent with the given configuration.
        :param config: A configuration object/dictionary containing deployment settings.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("DeploymentAgent initialized with configuration.")

        # Initialize OpenAI Client
        self.client = OpenAI(api_key=self.config.get("openai_api_key", ""))

    def generate_deployment_script(self):
        """
        Uses the OpenAI API to generate a complete deployment script in Python.
        The script should cover packaging the project and deploying it to a target environment.
        :return: The generated deployment script as a string.
        """
        self.logger.info("Generating deployment script using OpenAI API...")
        prompt = (
            "Generate a complete and optimized deployment script in Python that performs the following tasks:\n"
            "- Packages the project (e.g., creates a distributable archive or builds a Docker image)\n"
            "- Deploys the packaged project to a target environment (e.g., cloud deployment, Kubernetes, etc.)\n\n"
            "Include detailed comments, proper error handling, and clear step-by-step instructions."
        )
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert in cloud deployment and Python scripting."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=250,  # Adjust token limit as needed
            )
            generated_script = response.choices[0].message.content.strip()
            self.logger.info("Deployment script generated successfully.")
            return generated_script
        except Exception as e:
            self.logger.error(f"OpenAI API call failed for generating deployment script: {e}")
            return "No deployment script generated."

    def run_deployment(self):
        """
        Executes the deployment script generation process.
        :return: The generated deployment script as a string.
        """
        self.logger.info("Running deployment script generation process...")
        script = self.generate_deployment_script()
        return script

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",  # Replace with your actual API key
        "deployment_options": "Default deployment settings"
    }
    deployment_agent = DeploymentAgent(sample_config)
    deployment_script = deployment_agent.run_deployment()
    print("=== Generated Deployment Script ===")
    print(deployment_script)
