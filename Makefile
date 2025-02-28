.PHONY: test run

# Run unit tests using pytest
test:
	pytest --maxfail=1 --disable-warnings -q

# Run the entire development flow using main.py
run:
	python3 main.py --api-key "YOUR_OPENAI_API_KEY" --llm-backend "o1-mini" --research-topic "YOUR DEVELOPING IDEA"
