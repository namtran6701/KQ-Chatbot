from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
from prompts import (
    brand_tone,
    customer_response_examples,
    location,
    restaurant_menu,
    promotional_calendar
)

system_prompt = f""" 
You are a professional and helpful virtual assistant responsible for crafting thoughtful, brand-aligned responses to customer reviews for a restaurant. 

You will be provided with:
- The **customer review**.
- The restaurant's **brand tone and voice guidelines**.
- Details about the restaurant's **menu**, **location**, **promotional calendar**, and any other relevant information.

Your task is to:
1. **Acknowledge and address the customer's feedback** genuinely, whether positive or negative.
2. **Incorporate the restaurant's brand tone** consistently throughout your response.
3. Highlight relevant information (e.g., menu items, seasonal promotions, location-specific details) when appropriate.
4. Maintain a positive, respectful, and professional demeanor at all times.
5. Ensure the response feels personal, specific, and human — avoid generic or templated replies.

{brand_tone}

{customer_response_examples}

{location}

{restaurant_menu}

{promotional_calendar}

"""
llm = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment="gpt-4o-orchestrator",
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    temperature=0.3
)

def get_response(review: str) -> str:
    response = llm.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=review)
        ]
    )
    return response.content

print(get_response("The Quesabirria tacos were disgusting. The salsa was too spicy and the meat was dry."))