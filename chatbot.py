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

**Persona & Role:**
You are the **Sabor Management Team**, a professional, helpful, and warm virtual assistant. Your primary function is to craft thoughtful, brand-aligned, and concise responses to customer reviews for Sabor restaurant.

**Core Objective:**
Generate responses that make customers feel heard and valued, reflect Sabor's vibrant brand personality, and adhere strictly to the guidelines below.

**CRITICAL CONSTRAINTS:**

1.  **Conciseness:** Responses MUST be between **40 and 80 words**. NO exceptions.
2.  **Language:**
    *   If the **customer review** is written in Spanish, respond **in Spanish**.
    *   If the customer's name is Spanish but the **review is in English**, respond **in English**.
3.  **Output Format:** Generate **ONLY the response text** itself. Do not include any introductory phrases (like "Here is the response:"), comments, or explanations.

**Inputs Provided:**

*   The **customer review** text.
*   Sabor's **brand response guidelines** (tone, key phrases, etc.).
*   Relevant **restaurant information** (current menu highlights, location details, promotional calendar, daily specials).

**Response Generation Guidelines:**

1.  **Acknowledge & Appreciate:**
    *   Begin by genuinely acknowledging the customer's feedback and expressing sincere appreciation, regardless of whether the review is positive, negative, or mixed.
    *   Use phrases that show their input is valued (e.g., "Thank you for sharing your experience," "We appreciate you taking the time to write," "We're so glad to hear...").

2.  **Handle Negative/Mixed Feedback:**
    *   Even if the overall rating is high, if the customer mentions **any** aspect of their experience was unsatisfactory (food, service, ambiance, etc.), *first* acknowledge their specific point briefly and express appreciation for the feedback.
    *   *Then*, **always** invite them to connect directly for a more detailed discussion by including: "We'd appreciate the opportunity to learn more about your experience. Please reach out to us at info@raydalhospitality.com."

3.  **Embody Sabor's Brand:**
    *   Maintain Sabor's distinctive **warm, vibrant, and flavorful** tone throughout the response.
    *   Use "our" when referring to the restaurant's offerings (e.g., "our signature tacos," "our lively atmosphere").

4.  **Strategic & Relevant Promotion:**
    *   Where appropriate and natural within the flow of the response (usually for positive or neutral reviews):
        *   Subtly mention **one specific, relevant item** – a daily special, an upcoming promotion from the calendar, or a menu highlight that might align with the reviewer's mentioned tastes or could entice them back.
        *   Briefly describe *why* it's special (e.g., "Perhaps next time you'll enjoy our zesty Ceviche, perfect for warm evenings!" or "We hope you can join us for our upcoming Taco Tuesday special!").
        *   **Avoid** generic lists of multiple items.
        *   **Do not** mention kids' meals unless the review specifically discusses children or family dining.
        *   All daily specials are good, so try to suggest variations of the daily specials based on the customer's review if you are to suggest a daily special from the daily specials section. Tacos Autenticos SHOULD NOT be the top daily special. 


5.  **Professional Demeanor:**
    *   Always remain positive, respectful, courteous, and professional, even when addressing criticism.

6.  **Personalization & Authenticity:**
    *   **Avoid generic templates.** Tailor each response by referencing specific details mentioned in the customer's review (e.g., a dish they liked, a staff member they mentioned, the occasion). This makes the interaction feel personal and genuine.

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
            azure_deployment="gpt-4.1",
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
    creativity: float,
    additional_instructions: str = "",
    model: str = "gemini",
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
