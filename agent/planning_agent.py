import logging
import openai
from utils.logger import setup_logger  # Centralized logger from utils

class PlanningAgent:
    def __init__(self, config):
        """
        Initializes the Planning Agent with the given configuration.
        :param config: A configuration object/dictionary containing planning notes and settings.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("PlanningAgent initialized with configuration.")
        # Set up the OpenAI API key from configuration if provided.
        openai.api_key = self.config.get("openai_api_key", "")

    def gather_requirements(self):
        """
        Gathers project requirements from configuration or external notes.
        :return: A list of requirement strings.
        """
        self.logger.info("Gathering requirements...")
        # Read 'task_notes' from config; fallback to a default note if not provided.
        requirements = self.config.get('task_notes', ["Default Requirement: Setup project structure"])
        self.logger.info(f"Requirements gathered: {requirements}")
        return requirements

    def get_task_description(self, requirement):
        """
        Uses the OpenAI API to generate a detailed breakdown for a given requirement.
        :param requirement: A requirement string.
        :return: A detailed task description generated by the API.
        """
        try:
            self.logger.info("Querying OpenAI API for task refinement...")
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert software engineer."},
                    {"role": "user", "content": f"Provide a detailed breakdown of tasks required to fulfill the following requirement: {requirement}"}
                ],
                max_tokens=100
            )
            task_details = response.choices[0].message.content.strip()
            self.logger.info("Received detailed task description from OpenAI API.")
            return task_details
        except Exception as e:
            self.logger.error(f"OpenAI API call failed: {e}")
            return f"Process for '{requirement}' needs to be defined."

    def decompose_tasks(self, requirements):
        """
        Decomposes the requirements into actionable tasks.
        :param requirements: List of requirement strings.
        :return: A list of tasks (each task is a dictionary with details).
        """
        self.logger.info("Decomposing requirements into tasks...")
        tasks = []
        for req in requirements:
            # For each requirement, use the OpenAI API to generate a refined task breakdown.
            task_description = self.get_task_description(req)
            task = {"task": f"Handle: {req}", "details": task_description}
            tasks.append(task)
            self.logger.debug(f"Task created: {task}")
        self.logger.info("Task decomposition completed.")
        return tasks

    def formulate_plan(self):
        """
        Formulates a complete plan by combining requirement gathering and task decomposition.
        :return: A structured plan (list of tasks).
        """
        self.logger.info("Formulating the overall plan...")
        requirements = self.gather_requirements()
        tasks = self.decompose_tasks(requirements)
        self.logger.info("Plan formulation completed.")
        return tasks

# Example usage (for testing the module individually)
if __name__ == "__main__":
    # Sample configuration with task notes and an OpenAI API key.
    sample_config = {
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",  # Replace with your actual API key
        "task_notes": [
            "Setup development environment",
            "Implement core features",
            "Write unit tests",
            "Prepare deployment scripts"
        ]
    }
    planning_agent = PlanningAgent(sample_config)
    plan = planning_agent.formulate_plan()
    print("Generated Plan:")
    for task in plan:
        print(task)

