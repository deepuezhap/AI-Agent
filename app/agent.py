from google.adk.agents import Agent
import json
import litellm
litellm._turn_on_debug()  # Optional: see curl output

from google.adk.models.lite_llm import LiteLlm


with open("/Users/deepujoseph/Desktop/AI-Agent/app/faq.json", "r") as f:
    faq_data = json.load(f)


def search_faqs(query: str) -> str:
    for faq in faq_data:
        if query.lower() in faq["question"].lower():
            return f"Answer from FAQ: {faq['answer']}"
    return "Sorry, I couldn't find anything in the FAQ related to your question."


root_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),  # since local model, it is connected using ollama/chat
    name='root_agent',
    description='A helpful assistant clearing queries.',
    instruction=(
    "You are a Customer Support Agent."
    "Always use the `search_faqs` tool."
),

    tools=[search_faqs]

)
