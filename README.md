(still doing on the progress) 

# DevAutomator

DevAutomator is an AI-powered automated development pipeline that integrates planning, building, testing, deployment, and documentation generation—all orchestrated by specialized agents empowered by the OpenAI API.

## Overview

DevAutomator streamlines your development process by:
- **Planning:** Breaking down your developing ideas into actionable tasks.
- **Building:** Compiling and generating project code.
- **Testing:** Running unit tests and providing suggestions for improved coverage.
- **Deployment:** Packaging and deploying your project to target environments.
- **Documentation:** Generating and updating project documentation automatically.

The system is designed to be run with a single command, making it easy to initiate the entire development process from the command line.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/DevAutomator.git
    cd DevAutomator
    ```

2. **Set Up Python Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **(Optional) Docker Setup:**
    - Build the Docker image:
      ```bash
      docker build -t devautomator .
      ```
    - Run the container:
      ```bash
      docker run -e OPENAI_API_KEY="YOUR_OPENAI_API_KEY" -p 8080:8080 devautomator
      ```

## Usage

Run the development automation flow with a single command:

```bash
python3 main.py --api-key "YOUR_OPENAI_API_KEY" --llm-backend "o1-mini" --research-topic "YOUR DEVELOPING IDEA"
