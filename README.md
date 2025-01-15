# AI Assistant for GRC Queries

This project is a Flask-based AI assistant for handling grc queries about a application hosted on AWS. The assistant is compliant with frameworks like PCI DSS, NIST 800-53, NIST RMF, and NIST CSF.

## Features
- Answers compliance and security-related questions.
- Adheres to AWS security best practices.
- Easy-to-deploy REST API.

## Setup

### Prerequisites
- Python 3.8+
- OpenAI API Key
- Flask

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-assistant.git
   cd ai-assistant

2.Install dependencies:

pip install -r requirements.txt

3.Set your OpenAI API key:

export OPENAI_API_KEY=your_api_key

4.Run the application:

    python -m app.main

Deployment
Docker

    Build the Docker image:

docker build -t ai-assistant .

Run the container:

    docker run -p 5000:5000 ai-assistant

API Usage

    Endpoint: /query
    Method: POST
    Body:

{
  "query": "What is PCI DSS?"
}
