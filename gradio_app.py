import gradio as gr
from chatbot import get_response, format_review
from datetime import datetime

def generate_response(name, star_rating, review, review_date):
    if not review:
        return "Please enter a customer review first."
    if not name:
        return "Please enter the customer's name."
    if not star_rating:
        return "Please select a star rating."
    
    # Format the date to a nice string
    try:
        date_obj = datetime.strptime(review_date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")
    except:
        formatted_date = review_date
    
    review_dict = {
        "name": name,
        "star_rating": star_rating,
        "review": review,
        "date": formatted_date
    }
    return get_response(format_review(review_dict))

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")

# Create the Gradio interface
with gr.Blocks(title="Juan's Response Generator", theme=gr.themes.Base()) as app:
    gr.Markdown("# Juan's Response Generator")
    gr.Markdown("This tool helps generate professional, brand-aligned responses to customer reviews.")
    
    with gr.Row():
        with gr.Column():
            name_input = gr.Textbox(
                label="Customer Name:",
                placeholder="Enter customer's name...",
                lines=1
            )
            star_rating = gr.Slider(
                minimum=1,
                maximum=5,
                value=3,
                step=1,
                label="Star Rating"
            )
            review_date = gr.DateTime(
                label="Review Date",
                value=today,
            )
            review_input = gr.Textbox(
                label="Enter the customer review:",
                placeholder="Paste the customer review here...",
                lines=5
            )
            generate_btn = gr.Button("Generate Response", variant="primary")
        
        with gr.Column():
            response_output = gr.Textbox(
                label="Generated Response:",
                lines=10,
                interactive=False
            )
    
    generate_btn.click(
        fn=generate_response,
        inputs=[name_input, star_rating, review_input, review_date],
        outputs=response_output
    )
    
    gr.Markdown("---")
    gr.Markdown("Powered by Sales Factory | Juan's Response Generator")

if __name__ == "__main__":
    app.launch(share=True) 