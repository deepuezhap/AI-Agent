import requests
from bs4 import BeautifulSoup
import json

url = "https://www.nugenomics.in/faqs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

sections = soup.find_all('section', class_='aux-toggle-item')

faqs = []

for section in sections:
    question_tag = section.find('h4')
    answer_tag = section.find('p')
    
    if question_tag and answer_tag:
        question = question_tag.get_text(strip=True)
        answer = answer_tag.get_text(strip=True)
        faqs.append({"question": question, "answer": answer})

# Save the list of dictionaries to a JSON file
with open("faqs.json", "w", encoding="utf-8") as f:
    json.dump(faqs, f, ensure_ascii=False, indent=4)

print("FAQs saved successfully to faqs.json")
