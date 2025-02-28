# planning_agent.py

import logging
from utils.logger import setup_logger  # Assume we have a logger setup in utils/logger.py

class PlanningAgent:
    def __init__(self, config):
        """
        Initializes the Planning Agent with given configuration.
        :param config: A configuration object/dictionary containing planning notes and settings.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("PlanningAgent initialized with configuration.")

    def gather_requirements(self):
        """
        Gathers project requirements from configuration or external notes.
        :return: A list of requirement strings.
        """
        self.logger.info("Gathering requirements...")
        # Example: Read 'task_notes' from config if available
        requirements = self.config.get('task_notes', ["Default Requirement: Setup project structure"])
        self.logger.info(f"Requirements gathered: {requirements}")
        return requirements

    def decompose_tasks(self, requirements):
        """
        Decomposes the requirements into actionable tasks.
        :param requirements: List of requirement strings.
        :return: A list of tasks (each task can be a dict with details).
        """
        self.logger.info("Decomposing requirements into tasks...")
        tasks = []
        for req in requirements:
            # Here we split the requirement into a simple task with a description.
            task = {"task": f"Handle: {req}", "details": f"Process for '{req}' needs to be defined."}
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
    # Sample configuration with notes
    sample_config = {
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
