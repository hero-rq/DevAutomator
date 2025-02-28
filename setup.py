from setuptools import setup, find_packages

setup(
    name="DevAutomator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.65.1",
        "pytest>=7.0.0"
    ],
    entry_points={
        "console_scripts": [
            "devautomator=devautomator.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered automated development process.",
)
