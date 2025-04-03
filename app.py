import streamlit as st
from chatbot import get_response

# Set page config
st.set_page_config(
    page_title="Restaurant Review Response Generator",
    page_icon="🍽️",
    layout="centered"
)

# Add custom CSS
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and description
st.title("Juan's Response Generator")
st.markdown("""
    This tool helps generate professional, brand-aligned responses to customer reviews.
    Simply paste the customer's review below and click 'Generate Response'.
    """)

# Input area
review = st.text_area(
    "Enter the customer review:",
    placeholder="Paste the customer review here...",
    height=150
)

# Generate button
if st.button("Generate Response", type="primary"):
    if review:
        with st.spinner("Generating response..."):
            response = get_response(review)
            st.markdown("### Generated Response:")
            st.markdown(response)
    else:
        st.warning("Please enter a customer review first.")

# Add footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Powered by Sales Factory | Juan's Response Generator</p>
    </div>
    """, unsafe_allow_html=True) 