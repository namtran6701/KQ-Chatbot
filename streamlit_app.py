import streamlit as st
from chatbot import get_response, format_review
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Sabor's Review Response Generator", page_icon="💬", layout="wide"
)

# Title and description
st.title("Sabor's Review Response Generator")
st.markdown(
    "This tool helps generate professional, brand-aligned responses to customer reviews."
)

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    # Input fields
    review_date = st.date_input("Review Date", value=datetime.now())
    name = st.text_input("Customer Name:", placeholder="Enter customer's name...")
    star_rating = st.slider("Star Rating", min_value=1, max_value=5, value=3)
    review = st.text_area(
        "Enter the customer review:",
        placeholder="Paste the customer review here, leave blank if not provided.",
        height=150,
    )
    
    # Advanced Configuration in expander
    with st.expander("Advanced Configuration"):
        additional_instructions = st.text_area(
            "Additional Generation Instructions:",
            placeholder="Enter additional instructions to improve the response...",
            height=80,
        )
        creativity = st.slider(
            "Response Creativity", min_value=0.0, max_value=1.0, value=0.2, step=0.05
        )
        model = st.selectbox(
            "Response Model",
            options=["openai", "gemini"],
            index=0,
        )
    
    if st.button("Generate Response", type="primary"):
        # Check for name first
        if not name:
            st.error("Please enter the customer's name.")
        else:
            # If review is empty, set default based on star rating
            current_review = review
            if not current_review:
                if star_rating <= 2:
                    current_review = "negative experience"
                elif star_rating == 3:
                    current_review = "neutral experience"
                else:
                    current_review = "positive experience"
            
            # Format the date
            formatted_date = review_date.strftime("%B %d, %Y")

            # Create review dictionary
            review_dict = {
                "name": name,
                "star_rating": star_rating,
                "review": current_review,
                "date": formatted_date,
            }

            # Generate response
            response = get_response(
                format_review(review_dict),
                additional_instructions=additional_instructions,
                model=model,
                creativity=creativity,
            )

            # Display response in the second column
            with col2:
                st.text_area(
                    "Generated Response:", value=response, height=400, disabled=False
                )

# Footer
st.markdown("---")
st.markdown("Powered by Sales Factory | Sabor's Review Response Generator")
