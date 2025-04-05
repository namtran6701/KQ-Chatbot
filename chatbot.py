from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from prompts import (
    brand_tone,
    customer_response_examples,
    location,
    sabor_menu,
    sabor_promotional_calendar,
    sabor_food_allergens,
    sabor_daily_specials,
)

system_prompt = f""" 
You are a professional and helpful virtual assistant responsible for crafting thoughtful, brand-aligned responses to customer reviews for a restaurant. Don't be too lengthy and formal.

You will be provided with:
- The **customer review**.
- The restaurant's **brand tone and voice guidelines**.
- Details about the restaurant's **menu**, **location**, **promotional calendar**, **daily specials**, and any other relevant information.

Your task is to:
1. **Acknowledge and address the customer's feedback** genuinely, whether positive or negative.
2. **Incorporate the restaurant's brand tone** consistently throughout your response.
3. Highlight relevant information (e.g., menu items, daily specials, promotional calendar, location-specific details) when appropriate.
4. Maintain a positive, respectful, and professional demeanor at all times.
5. Ensure the response feels personal, specific, and human — avoid generic or templated replies.

{brand_tone}

{customer_response_examples}

{location}

{sabor_menu}

{sabor_daily_specials}

{sabor_promotional_calendar}

{sabor_food_allergens}


"""
llm = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_deployment="gpt-4o-orchestrator",
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    temperature=0.3,
    max_tokens=200,
)
llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro-exp-03-25",
    temperature=0,
    max_tokens=200,
    timeout=None,
    max_retries=2,
    api_key=os.environ["GEMINI_API_KEY"],
)


def format_review(review: dict) -> str:
    """Convert a review dictionary into a formatted text string."""
    date_str = review.get("date", "")  # Get date if it exists, otherwise empty string
    date_prefix = f" on {date_str}" if date_str else ""
    return f"Review from {review['name']}{date_prefix} ({review['star_rating']} stars):\n{review['review']}"


def get_response(review: str, model="openai") -> str:
    # If review is already a formatted string, use it directly
    if isinstance(review, str):
        review_text = review
    # If review is a dictionary, format it
    elif isinstance(review, dict):
        review_text = format_review(review)
    else:
        raise ValueError("Review must be either a string or a dictionary")
    if model == "openai":
        response = llm.invoke(
            [SystemMessage(content=system_prompt), HumanMessage(content=review_text)]
        )
    else:
        response = llm_gemini.invoke(
            [("system", system_prompt), ("human", review_text)]
        )
    return response.content


# Test with a dictionary
review = {
    "name": "Lionel Ronaldo",
    "star_rating": 1,
    "review": "The Quesabirria tacos were disgusting. The salsa was too spicy and the meat was dry.",
}
print(get_response(review))
