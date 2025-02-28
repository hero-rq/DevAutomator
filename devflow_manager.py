import logging
from agents.planning_agent import PlanningAgent
from agents.build_agent import BuildAgent
from agents.test_agent import TestAgent
from agents.deployment_agent import DeploymentAgent
from agents.documentation_agent import DocumentationAgent
from utils.logger import setup_logger

class DevFlowManager:
    def __init__(self, config):
        """
        Initializes the DevFlowManager with the given configuration.
        :param config: A configuration object/dictionary containing settings for all phases.
        """
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("DevFlowManager initialized.")

        # Instantiate all agents with the shared configuration.
        self.planning_agent = PlanningAgent(config)
        self.build_agent = BuildAgent(config)
        self.test_agent = TestAgent(config)
        self.deployment_agent = DeploymentAgent(config)
        self.documentation_agent = DocumentationAgent(config)

    def run_development_flow(self):
        """
        Orchestrates the complete development workflow by invoking each agent in sequence.
        :return: True if the entire flow is successful, False otherwise.
        """
        self.logger.info("Starting development flow...")

        # Phase 1: Planning
        plan = self.planning_agent.formulate_plan()
        self.logger.info(f"Generated Plan: {plan}")

        # Phase 2: Build
        build_result = self.build_agent.run_build()
        if not build_result:
            self.logger.error("Build phase failed. Aborting development flow.")
            return False

        # Phase 3: Testing
        test_result = self.test_agent.run_tests()
        if not test_result:
            self.logger.error("Testing phase failed. Aborting development flow.")
            return False

        # Phase 4: Deployment
        deployment_result = self.deployment_agent.run_deployment()
        if not deployment_result:
            self.logger.error("Deployment phase failed. Aborting development flow.")
            return False

        # Phase 5: Documentation
        project_summary = (
            "DevAutomator is an automated development process that integrates planning, "
            "building, testing, deployment, and documentation generation using AI-powered agents."
        )
        code_structure = self.get_code_structure_summary()
        documentation = self.documentation_agent.generate_documentation(project_summary, code_structure)
        doc_update_success = self.documentation_agent.update_documentation_file(documentation)
        if not doc_update_success:
            self.logger.error("Documentation update failed.")
        else:
            self.logger.info("Documentation updated successfully.")

        self.logger.info("Development flow completed successfully.")
        return True

    def get_code_structure_summary(self):
        """
        Provides a summary of the project's code structure.
        :return: A string representing the project's directory layout.
        """
        code_structure = (
            "DevAutomator/\n"
            "├── main.py\n"
            "├── config.py\n"
            "├── devflow_manager.py\n"
            "├── requirements.txt\n"
            "├── setup.py\n"
            "├── Makefile\n"
            "├── Dockerfile\n"
            "├── README.md\n"
            "├── LICENSE\n"
            "├── agents/\n"
            "│   ├── planning_agent.py\n"
            "│   ├── build_agent.py\n"
            "│   ├── test_agent.py\n"
            "│   ├── deployment_agent.py\n"
            "│   └── documentation_agent.py\n"
            "└── utils/\n"
            "    ├── logger.py\n"
            "    └── helper_functions.py\n"
        )
        return code_structure

# Example usage (for standalone testing)
if __name__ == "__main__":
    sample_config = {
        "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",  # Replace with your actual API key
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
    manager = DevFlowManager(sample_config)
    flow_success = manager.run_development_flow()
    print("Development Flow Result:", "Success" if flow_success else "Failure")
