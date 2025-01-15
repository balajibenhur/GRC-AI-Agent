import openai
from flask import Blueprint, request, jsonify
import os

main_bp = Blueprint('main', __name__)

# Set your OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

@main_bp.route('/query', methods=['POST'])
def handle_query():
    """
    Handle client queries and provide AI assistant responses.
    """
    def ai_assistant(query):
        context = (
            "You are an AI assistant designed to answer client queries about a payment processing platform hosted on AWS. "
            "The platform adheres to compliance frameworks such as PCI DSS, NIST 800-53, NIST RMF, and NIST CSF. "
            "Additionally, the platform follows AWS best practices for security, including implementing IAM policies, data encryption, "
            "network segmentation, and continuous monitoring. Answer queries in a professional and concise manner."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": query},
                ],
                max_tokens=500,
                temperature=0.7,
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"An error occurred: {e}"

    data = request.json
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request. Please provide a 'query' field."}), 400

    query = data['query']
    response = ai_assistant(query)
    return jsonify({"response": response})
