import os
import logging
from agents.planning_agent import PlanningAgent
from agents.build_agent import BuildAgent
from agents.test_agent import TestAgent
from agents.deployment_agent import DeploymentAgent
from agents.documentation_agent import DocumentationAgent

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - [%(name)s] %(message)s"))
    logger.addHandler(handler)
    return logger

class DevFlowManager:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(__name__)
        self.logger.info("DevFlowManager initialized.")

        self.agents = {
            "planning": PlanningAgent(config),
            "build": BuildAgent(config),
            "test": TestAgent(config),
            "deployment": DeploymentAgent(config),
            "documentation": DocumentationAgent(config)
        }

    def run_development_flow(self):
        self.logger.info("Starting development flow...")
        results = {}

        try:
            plan = self.agents["planning"].formulate_plan()
            self.logger.info(f"Generated Plan: {plan}")
            results["planning"] = "Success"
        except Exception as e:
            self.logger.error(f"Planning phase failed: {e}")
            results["planning"] = "Failed"

        for phase in ["build", "test", "deployment", "documentation"]:
            try:
                method = "run_tests" if phase == "test" else "generate_documentation" if phase == "documentation" else f"run_{phase}"
                success = getattr(self.agents[phase], method)()
                results[phase] = "Success" if success else "Failed"
            except Exception as e:
                self.logger.error(f"{phase.capitalize()} phase failed: {e}")
                results[phase] = "Failed"

        self.logger.info("Development flow completed.")
        return results

    def get_code_structure_summary(self, base_dir="."):
        tree_str = ""
        for root, dirs, files in os.walk(base_dir):
            level = root.replace(base_dir, "").count(os.sep)
            indent = " " * (level * 4)
            tree_str += f"{indent}{os.path.basename(root)}/\n"
            sub_indent = " " * ((level + 1) * 4)
            for f in files:
                tree_str += f"{sub_indent}{f}\n"
        return tree_str
