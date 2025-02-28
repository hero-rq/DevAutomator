import logging
import subprocess
from openai import OpenAI  # OpenAI v1.x client
from utils.logger import setup_logger  # Centralized logger from utils

class TestAgent:
    def __init__(self, config):
        """
        Initializes the Test Agent with the given configuration.
        :param config: A configuration object/dictionary containing test settings.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("TestAgent initialized with configuration.")

        # Initialize OpenAI Client
        self.client = OpenAI(api_key=self.config.get("openai_api_key", ""))

    def run_unit_tests(self):
        """
        Executes unit tests for the project.
        :return: Boolean indicating whether the tests passed.
        """
        self.logger.info("Running unit tests...")
        try:
            # Running pytest with safer subprocess handling
            result = subprocess.run(
                ["pytest", "--maxfail=1", "--disable-warnings", "-q"],
                capture_output=True,
                text=True,
                check=False  # Allow failures without crashing
            )
            self.logger.info("Unit test output:\n" + result.stdout.strip())
            if result.stderr:
                self.logger.warning("Unit test errors:\n" + result.stderr.strip())

            if result.returncode == 0:
                self.logger.info("Unit tests passed successfully.")
                return True
            else:
                self.logger.error("Unit tests failed.")
                return False
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Unit test execution failed: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error while running tests: {e}")
            return False

    def get_test_suggestions(self, project_details):
        """
        Uses the OpenAI API to generate test suggestions or validate test coverage.
        :param project_details: A description of the project or tests.
        :return: Suggestions as a string.
        """
        try:
            self.logger.info("Querying OpenAI API for test suggestions...")
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert software testing engineer."},
                    {"role": "user", "content": f"Based on the following project details, provide test suggestions to ensure thorough coverage: {project_details}"}
                ],
                max_tokens=150
            )
            suggestions = response.choices[0].message.content.strip()
            self.logger.info("Received test suggestions from OpenAI API.")
            return suggestions
        except Exception as e:
            self.logger.error(f"OpenAI API call failed for test suggestions: {e}")
            return "No suggestions available."

    def run_tests(self):
        """
        Executes the full test suite including unit tests and optionally integration tests.
        :return: True if all tests pass, False otherwise.
        """
        self.logger.info("Running complete test suite...")
        unit_test_result = self.run_unit_tests()

        # Optionally: Use OpenAI API to suggest improvements or additional tests
        project_details = "Project setup and current test coverage details."
        suggestions = self.get_test_suggestions(project_details)
        self.logger.info(f"Test suggestions: {suggestions}")
        return unit_test_result

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",  # Replace with your actual API key
        "test_options": "Default test settings"
    }
    test_agent = TestAgent(sample_config)
    tests_passed = test_agent.run_tests()
    print("Tests result:", "Passed" if tests_passed else "Failed")

