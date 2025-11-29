import os
from openai import OpenAI

# Load environment variables
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not api_key:
    raise RuntimeError("Set OPENAI_API_KEY environment variable before running the agent.")

# Initialize client
client = OpenAI(api_key=api_key)

def ask_agent(question):
    try:
        response = client.responses.create(
            model=model,
            input=question  # Responses API expects plain text
        )

        # Safely extract the model output
        return response.output[0].content[0].text

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    try:
        user_input = input("You: ")
        answer = ask_agent(user_input)
        print("AI:", answer)
    except Exception as e:
        print("API error:", e)
