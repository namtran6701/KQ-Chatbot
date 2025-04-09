from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import streamlit as st
from prompts import (
    brand_tone,
    customer_response_examples,
    location,
    sabor_menu,
    sabor_promotional_calendar,
    sabor_food_allergens,
    sabor_daily_specials,
)

# SECRETS FOR STREAMLIT
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
AZURE_OPENAI_ENDPOINT = st.secrets["AZURE_OPENAI_ENDPOINT"]
AZURE_OPENAI_API_VERSION = st.secrets["AZURE_OPENAI_API_VERSION"]
AZURE_OPENAI_API_KEY = st.secrets["AZURE_OPENAI_API_KEY"]

# local secrets
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
# AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
# AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")


def get_system_prompt(additional_instructions: str = "") -> str:
    return f""" 
Your name is Sabor Management Team.

You are a professional and helpful virtual assistant responsible for crafting thoughtful, brand-aligned, concise responses to customer reviews for Sabor restaurant. 
Be concise and to the point. Maximum 100-110 words. AVOID EXCEED THIS LIMIT.

if the review is in spanish, respond in spanish. However, if only the customer's name is in spanish, but the review is in english, YOU MUST respond in english.


You will be provided with:
- The **customer review**.
- The restaurant's **brand's response guidelines**.
- Details about the restaurant's **menu**, **location**, **promotional calendar**, **daily specials**, and any other relevant information.

Your task is to:
1. **Genuinely Acknowledge the Customer's Feedback**  
   Whether the feedback is positive or negative, respond with sincerity and appreciation. Demonstrate that their voice is heard and valued.

2. **Reflect the Restaurant's Brand Tone**  
   Ensure your response embodies *Sabor's* distinctive voice — warm, vibrant, and full of flavor. Stay consistent with the brand's personality in every interaction.

3. **Promote Daily Specials and Menu Highlights**  
   Whenever appropriate, mention *Sabor's* daily specials, upcoming promotions from the calendar, or recommend standout items from the menu to drive engagement and interest.

4. **Maintain a Positive, Respectful, and Professional Demeanor**  
   Regardless of the tone or content of the feedback, remain courteous, calm, and uplifting in your language.

5. **Make Every Response Feel Personal and Authentic**  
   Avoid generic templates. Tailor your replies to the individual — reference specific points from their message and respond with warmth and humanity.

IMPORTANT: This is the additional instructions that you MUST follow (if any):
{additional_instructions}

--------------------------------
Below are the brand tone, customer response examples, menu, daily specials, promotional calendar, and food allergens for the restaurant:

{brand_tone}

{customer_response_examples}

{sabor_menu}

{sabor_daily_specials}

{sabor_promotional_calendar}

{sabor_food_allergens}

{location}
"""


def get_llm_models(model: str = "openai", creativity: float = 0.2):
    if model == "openai":
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            azure_deployment="gpt-4o-orchestrator",
            openai_api_version=AZURE_OPENAI_API_VERSION,
            api_key=AZURE_OPENAI_API_KEY,
            temperature=creativity,
            max_tokens=200,
        )
        return llm
    elif model == "gemini":
        llm_gemini = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro-exp-03-25",
            temperature=creativity,
            timeout=None,
            max_retries=2,
            max_tokens=None,  # reasoning model, shouldn't set a max tokens
            api_key=GEMINI_API_KEY,
        )
        return llm_gemini


def format_review(review: dict) -> str:
    """Convert a review dictionary into a formatted text string with clear sections for each piece of information."""
    date_str = review.get("date", "Not specified")  # Get date if it exists, otherwise indicate it's not specified
    return (
        f"Customer Name: {review['name']}\n"
        f"Date: {date_str}\n"
        f"Rating: {review['star_rating']} stars\n"
        f"Review:\n{review['review']}"
    )


def get_response(
    review: str,
    additional_instructions: str = "",
    model: str = "openai",
    creativity: float = 0.2,
) -> str:
    # If review is already a formatted string, use it directly
    if isinstance(review, str):
        review_text = review
    # If review is a dictionary, format it
    elif isinstance(review, dict):
        review_text = format_review(review)
    else:
        raise ValueError("Review must be either a string or a dictionary")

    system_prompt = get_system_prompt(additional_instructions)

    llm = get_llm_models(model=model, creativity=creativity)
    if model == "openai":
        response = llm.invoke(
            [SystemMessage(content=system_prompt), HumanMessage(content=review_text)]
        )
    elif model == "gemini":
        response = llm.invoke(
            [
                (
                    "system",
                    system_prompt,
                ),
                (
                    "human",
                    review_text,
                ),
            ]
        )
    return response.content


# Test with a dictionary
# review = {
#     "name": "Lionel Ronaldo",
#     "star_rating": 1,
#     "review": "The Quesabirria tacos were disgusting. The salsa was too spicy and the meat was dry.",
# }
# print(get_response(review, model="gemini"))



# todo: handle cases where the review is empty, only name and star rating is provided
# todo: validate model's name is correct
