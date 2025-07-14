import json
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')  # small and fast

# Load FAQ
with open('/Users/deepujoseph/Desktop/AI-Agent/app/faq.json','r') as f:
    faq_data = json.load(f)

faq_questions = [item['question'] for item in faq_data]
faq_answers = [item['answer'] for item in faq_data]




# Embed questions
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

print(get_faq_answer("what do we do"))