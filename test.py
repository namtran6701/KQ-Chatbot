# in this file, I will compare the quality of responses from the gemini and openai models

import pandas as pd
import time
from chatbot import get_response

five_star_review = {
    "review": "I love this place! The food is amazing and the service is great. I will definitely be back.",
    "star_rating": 5,
    "date": "2025-04-18",
    "name": "Juan Hernandez"
}

three_star_review = {
    "review": "The food was good, but the service was slow and the staff was not very friendly.",
    "star_rating": 3,
    "date": "2025-04-18",
    "name": "Juan Hernandez"
}

one_star_review = {
    "review": "The food was terrible and the service was slow and the staff was not very friendly.",
    "star_rating": 1,
    "date": "2025-04-18",
    "name": "Juan Hernandez"
}

reviews = [five_star_review, three_star_review, one_star_review]
results = []
num_responses_per_review = 1

for review in reviews:
    review_text = review['review']
    for i in range(num_responses_per_review):
        time.sleep(2)
        # You might want to adjust temperature or other parameters for variety
        response_gemini = get_response(review, 0.4, "", "gemini") 
        response_openai = get_response(review, 0.4, "", "openai") 
        
        results.append({
            "Review": review_text,
            "Gemini Response": response_gemini,
            "OpenAI Response": response_openai
        })

# Create DataFrame
df = pd.DataFrame(results)

# Export to Excel
excel_filename = "model_comparison.xlsx"
df.to_excel(excel_filename)

print(f"Generated {len(results)} responses and saved to {excel_filename}")








