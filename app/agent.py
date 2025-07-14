from google.adk.agents import Agent
import json
import litellm
from google.adk.models.lite_llm import LiteLlm
from sentence_transformers import SentenceTransformer, util
import datetime

model = SentenceTransformer('all-MiniLM-L6-v2')   #load the model for converting text to vector embeddings


with open("/Users/deepujoseph/Desktop/AI-Agent/app/faq.json", "r") as f: # load the data from the json file
    faq_data = json.load(f)


faq_questions = [item['question'] for item in faq_data]
faq_answers = [item['answer'] for item in faq_data]

faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

def get_faq_answer(user_question, threshold=0.5):
    query_embedding = model.encode(user_question, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, faq_embeddings)[0]
    best_score_idx = int(scores.argmax())
    best_score = float(scores[best_score_idx])

    if best_score > threshold:
        return faq_answers[best_score_idx]
    else:
        return "Sorry, I don't know the answer to that."



root_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),  # since local model, it is connected using ollama/chat
    name='root_agent',
    description='A helpful assistant clearing queries.',
    instruction=(
    "You are a Customer Support Agent for Nugenomics.\n\n"
    "You are provided with relevant FAQ question-answer pairs via the `search_faqs` tool — always use this tool to respond.\n"
    "Combine answers naturally into a human-like conversation. Do not repeat or number them (avoid '1.', '2.', etc).\n"
    "Explain professionally.\n\n"
    "If the FAQ tool returns: 'No relevant FAQ found for this query', then simply say that and do not try to make up an answer."
),

    tools=[search_faqs]

)

