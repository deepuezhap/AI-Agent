import json
from sentence_transformers import SentenceTransformer, util
from functools import lru_cache
import logging
# Load model
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


def get_faq_answer(user_question, threshold=0.5):
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
        return "Sorry, I don't know the answer to that."          # if similarity score is below threshold for both case just say i dont know.LLm will handle rest


