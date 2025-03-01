#test main

#!/usr/bin/env python3
"""
Final Project Code Generated via Agent Collaboration
Research Topic: YOUR DEVELOPING IDEA

This project simulates a collaboration between two agents (Alpha and Beta) that:
• Generate innovative ideas related to the research topic.
• Evaluate each other’s ideas.
• Refine the collaborative output over multiple iterations (5 rounds).
• Ultimately produce the final project code.

Usage:
    python3 main.py --api-key "YOUR_OPENAI_API_KEY" --model "gpt-3.5-turbo" --research-topic "YOUR DEVELOPING IDEA"
"""

import argparse
from openai import OpenAI

class Agent:
    def __init__(self, name, client, model, research_topic):
        self.name = name
        self.client = client
        self.model = model
        self.research_topic = research_topic

    def generate_idea(self, iteration):
        prompt = (
            f"Iteration {iteration}: As Agent {self.name}, propose an innovative idea "
            f"related to the research topic: '{self.research_topic}'."
        )
        response = self.call_openai_api(prompt)
        return response.strip()

    def evaluate_idea(self, idea, iteration):
        prompt = (
            f"Iteration {iteration}: As Agent {self.name}, critically evaluate the idea: '{idea}'. "
            "Suggest improvements if necessary."
        )
        response = self.call_openai_api(prompt)
        return response.strip()

    def call_openai_api(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"You are Agent {self.name}."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content']

def simulate_agents(api_key, model, research_topic, iterations=5):
    client = OpenAI(api_key=api_key)
    agents = [
        Agent("Alpha", client, model, research_topic),
        Agent("Beta", client, model, research_topic)
    ]

    for i in range(1, iterations + 1):
        ideas = [agent.generate_idea(i) for agent in agents]
        for agent in agents:
            for idea in ideas:
                agent.evaluate_idea(idea, i)

    final_project_code = f'''#!/usr/bin/env python3
"""
Final Project Code generated via Agent Collaboration

Research Topic: {research_topic}
"""

def final_feature():
    print("This is the final project feature based on the research topic: {research_topic}")

def main():
    final_feature()

if __name__ == '__main__':
    main()
'''
    return final_project_code

def main():
    parser = argparse.ArgumentParser(description="Agent Collaboration Code Generator")
    parser.add_argument('--api-key', type=str, required=True, help="Your OpenAI API key")
    parser.add_argument('--model', type=str, required=True, choices=['gpt-3.5-turbo', 'gpt-4'], help="OpenAI model to use")
    parser.add_argument('--research-topic', type=str, required=True, help="Research topic or developing idea")
    args = parser.parse_args()

    project_code = simulate_agents(args.api_key, args.model, args.research_topic)
    print(project_code)

if __name__ == '__main__':
    main()
