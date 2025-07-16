from google.adk.agents import Agent
import json
from google.adk.models.lite_llm import LiteLlm
from sentence_transformers import SentenceTransformer, util
import logging
from functools import lru_cache

model = SentenceTransformer('all-MiniLM-L6-v2')  # small and fast


@lru_cache(maxsize=1)
def load_faq_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            if not data:
                raise ValueError("FAQ data is empty")
            return data
    except Exception as e:
        logging.error(f"Error loading FAQ data: {str(e)}")
        raise

faq_data = load_faq_data("/Users/deepujoseph/Desktop/AI-Agent/app/faq.json")

faq_questions = [item['question'] for item in faq_data]
faq_answers = [item['answer'] for item in faq_data]



# Embed questions
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)
faq_ans_embeddings = model.encode(faq_answers, convert_to_tensor=True)


def get_faq_answer(user_question : str)-> str:
    threshold=0.5
    user_question = user_question.strip().lower()
    query_embedding = model.encode(user_question, convert_to_tensor=True) #embeding of user query


    question_scores = util.cos_sim(query_embedding, faq_embeddings)[0]  # finding similarity between query and question
    
    best_score_idx = int(question_scores.argmax())
    best_score = float(question_scores[best_score_idx])

    if best_score > threshold:
        return faq_answers[best_score_idx]
    else:
        answer_scores = util.cos_sim(query_embedding, faq_ans_embeddings)[0]    # finding similarity between query and answers
        best_score_idx = int(answer_scores.argmax())
        best_score = float(answer_scores[best_score_idx])                   # if we cant find similarity between question , compare with answers too 
        if best_score > threshold:
            return faq_answers[best_score_idx]
        return ''          # if similarity score is below threshold for both case just say i dont know.LLm will handle rest


root_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),  # since local model, it is connected using ollama/chat
    name='root_agent',
    description='A helpful assistant clearing queries.',
    instruction=(
        "You are a Customer Support Agent for NuGenomics. Your responses must be:\n"
        "- Accurate (only use get_faq_answer tool)\n"
        "- Professional\n"
        "- Concise (1-2 paragraphs max)\n\n"
        
        "Rules:\n"
        "1. ALWAYS use the get_faq_answer tool for responses\n"
        "2. If the tool returns no answer, say: 'I couldn't find that information. "
        "Please contact support@nugenomics.in for further assistance.'\n"
        "3. Never invent, speculate, or provide unofficial information\n\n"
    ),

tools=[get_faq_answer]
)

