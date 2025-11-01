import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer
model_name = "Ayaan-Sharif/t5-spelling-corrector-finetuned-v3"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def correct_spelling(text):
    """
    Corrects spelling errors in financial text using T5 model.
    
    Args:
        text: Input text with potential spelling errors
        
    Returns:
        Corrected text
    """
    if not text.strip():
        return "Please enter some text to correct."
    
    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate correction
    outputs = model.generate(
        **inputs,
        max_length=50,
        num_beams=4,
        early_stopping=True
    )
    
    # Decode output
    corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return corrected

# Example inputs for demonstration
examples = [
    ["One Hunderd Thousand Rupees"],
    ["Five Laakh Twenty Three Thousand Rupees"],
    ["Ten Cor e Fifty Six Laakh Rupees"],
    ["Twenti Five Thousnd Three Hundad Rupees"],
    ["One krore thosand rupees"],
]

# Create Gradio interface
with gr.Blocks(title="T5 Spelling Corrector - Indian Financial Text") as demo:
    gr.Markdown("""
    # T5 Spelling Corrector for Indian Financial Text
    
    This model corrects spelling errors in Indian financial documents, particularly focusing on:
    - Monetary amounts (Crore, Lakh, Thousand, Hundred)
    - Currency terms (Rupees, Paise)
    - OCR errors from scanned documents
    
    **Model:** [Ayaan-Sharif/t5-spelling-corrector-finetuned-v3](https://huggingface.co/Ayaan-Sharif/t5-spelling-corrector-finetuned-v3)
    """)
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Input Text (with spelling errors)",
                placeholder="Enter text with potential spelling errors...",
                lines=3
            )
            submit_btn = gr.Button("Correct Spelling", variant="primary")
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Corrected Text",
                lines=3
            )
    
    gr.Examples(
        examples=examples,
        inputs=input_text,
        outputs=output_text,
        fn=correct_spelling,
        cache_examples=True,
    )
    
    submit_btn.click(
        fn=correct_spelling,
        inputs=input_text,
        outputs=output_text
    )
    
    gr.Markdown("""
    ### About
    This model has been fine-tuned on 9,000+ samples of Indian financial documents to correct:
    - OCR errors from scanned invoices and receipts
    - Phonetic misspellings in monetary amounts
    - Common variations in Indian financial terminology
    
    ### Limitations
    - Optimized for Indian financial text; may not work well on general English
    - Best suited for monetary amounts and financial terminology
    - Performance depends on severity of spelling errors
    """)

if __name__ == "__main__":
    demo.launch()
