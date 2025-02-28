import logging
import subprocess
from utils.logger import setup_logger  # Centralized logger from utils
from openai import OpenAI  # OpenAI v1.x client

class DeploymentAgent:
    def __init__(self, config):
        """
        Initializes the Deployment Agent with the given configuration.
        :param config: A configuration object/dictionary containing deployment settings.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("DeploymentAgent initialized with configuration.")

        # Initialize OpenAI Client
        self.client = OpenAI(api_key=self.config.get("openai_api_key", ""))

    def package_project(self):
        """
        Packages the project for deployment.
        This could be creating a distributable archive or building a Docker image.
        :return: Boolean indicating whether packaging was successful.
        """
        self.logger.info("Packaging the project for deployment...")
        try:
            # Replace this with actual packaging commands (e.g., tar, zip, docker build)
            result = subprocess.run(["echo", "Packaging simulated..."], capture_output=True, text=True, check=True)
            self.logger.info("Packaging output:\n" + result.stdout.strip())
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Packaging command failed: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error in packaging: {e}")
            return False

    def deploy_project(self):
        """
        Deploys the packaged project to a target environment.
        :return: Boolean indicating whether the deployment was successful.
        """
        self.logger.info("Starting project deployment...")
        try:
            # Replace with real deployment commands (e.g., `kubectl apply`, `scp`, `rsync`)
            result = subprocess.run(["echo", "Deployment simulated..."], capture_output=True, text=True, check=True)
            self.logger.info("Deployment output:\n" + result.stdout.strip())
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Deployment command failed: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error in deployment: {e}")
            return False

    def get_deployment_feedback(self, project_details):
        """
        Uses the OpenAI API to get suggestions for improving the deployment process.
        :param project_details: A description of the project or deployment details.
        :return: Suggestions as a string.
        """
        try:
            self.logger.info("Querying OpenAI API for deployment suggestions...")
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert in cloud deployment."},
                    {"role": "user", "content": f"Suggest improvements for this deployment setup: {project_details}"}
                ],
                max_tokens=100
            )
            suggestions = response.choices[0].message.content.strip()
            self.logger.info("Received deployment suggestions from OpenAI API.")
            return suggestions
        except Exception as e:
            self.logger.error(f"OpenAI API call failed for deployment suggestions: {e}")
            return "No suggestions available."

    def run_deployment(self):
        """
        Executes the full deployment process including packaging and deployment.
        :return: True if deployment was successful, False otherwise.
        """
        self.logger.info("Running full deployment process...")
        package_success = self.package_project()
        if not package_success:
            self.logger.error("Packaging failed. Aborting deployment.")
            return False

        deploy_success = self.deploy_project()
        # Include deployment details for AI feedback
        project_details = "Project setup: CI/CD pipeline, environment details, deployment target."
        suggestions = self.get_deployment_feedback(project_details)
        self.logger.info(f"Deployment suggestions: {suggestions}")
        return deploy_success

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",  # Replace with your actual API key
        "deployment_options": "Default deployment settings"
    }
    deployment_agent = DeploymentAgent(sample_config)
    deployment_result = deployment_agent.run_deployment()
    print("Deployment result:", "Success" if deployment_result else "Failure")
