# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port if needed (optional)
EXPOSE 8080

# Define environment variable for OpenAI API key (adjust as needed)
ENV OPENAI_API_KEY=YOUR_OPENAI_API_KEY

# Run main.py when the container launches
CMD ["python", "main.py", "--api-key", "$OPENAI_API_KEY", "--llm-backend", "o1-mini", "--research-topic", "YOUR DEVELOPING IDEA"]
