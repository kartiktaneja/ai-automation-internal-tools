import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an internal support knowledgebase assistant.

Your task is to analyze unstructured customer support text and extract
structured knowledge in JSON format.

Return a JSON array. Each object must contain:
- issue (string)
- category (string)
- symptoms (list of strings)
- possible_causes (list of strings)
- resolution_steps (list of strings)

Rules:
- Only return valid JSON
- Do not include explanations
- Be concise and practical
"""

def analyze_support_text(raw_text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": raw_text}
        ]
    )

    return json.loads(response.choices[0].message.content)


def main():
    with open("ai_knowledgebase_builder/input/raw_text.txt", "r") as f:
        raw_text = f.read()

    structured_data = analyze_support_text(raw_text)

    with open("ai_knowledgebase_builder/output/structured_knowledge.json", "w") as f:
        json.dump(structured_data, f, indent=2)

    print("Structured knowledge base generated successfully.")


if __name__ == "__main__":
    main()
