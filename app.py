import gradio as gr
import google.generativeai as genai
import os

# --- Configuration ---
# IMPORTANT: Paste your Google Gemini API Key here.
# For production, it's better to use environment variables.
GOOGLE_API_KEY = "AIzaSyDWKE7ml4qIjKDcN-bly3J-uOPRkuy7IFM"
genai.configure(api_key=GOOGLE_API_KEY)

# --- Model Initialization ---
# Using the latest Flash model for speed and capability
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Core Logic with History ---
def generate_answer(message, history):
    """
    This function takes a user's message and the conversation history,
    sends it to the Gemini API, and returns the response.
    """
    if not message:
        return "Please ask a question."

    # This is the prompt engineering part.
    # We create a system prompt to guide the model's behavior.
    prompt = f"""
    You are an expert Python programming assistant. Your goal is to answer questions clearly, 
    provide concise code examples, and explain concepts simply. 
    Do not answer questions that are not about Python.
    
    User's question: "{message}"
    """
    
    try:
        # The model.generate_content method can take the prompt directly
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I encountered an error. Please check your API key or try again."

# --- Custom CSS for a modern look ---
custom_css = """
/* General container styling */
#chatbot {
    font-family: 'Inter', sans-serif;
    border: none;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
    border-radius: 12px;
}
/* Chat message styling */
.gradio-container .prose {
    font-size: 16px !important; /* Increase base font size */
}
/* Code block styling */
.prose pre {
    background-color: #f0f4f8; /* Light blue-gray background for code */
    border: 1px solid #d1d5db;
    border-radius: 8px;
    padding: 12px;
}
.prose code {
    font-family: 'Fira Code', 'monospace' !important; /* Use a coding font */
    font-size: 14px !important;
}
"""

# --- Gradio Interface ---
# Using gr.ChatInterface for a ChatGPT-like experience
iface = gr.ChatInterface(
    fn=generate_answer,
    chatbot=gr.Chatbot(
        height=500,
        show_label=False,
        avatar_images=(None, "https://placehold.co/40x40/000000/FFFFFF?text=🤖") # (user, bot)
    ),
    textbox=gr.Textbox(
        placeholder="Ask me anything about Python...", 
        container=False, 
        scale=7
    ),
    title="🐍 Python Expert Chatbot",
    description="This chatbot uses Google's Gemini API to answer any question about Python.",
    theme=gr.themes.Default(
        primary_hue="blue", 
        secondary_hue="blue",
        font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"]
    ),
    css=custom_css,
    submit_btn="➤ Send",
    retry_btn=None,
    undo_btn=None,
    clear_btn="Clear Conversation",
)

# --- Launch the App ---
if __name__ == "__main__":
    # This tells Gradio to be accessible from outside the Docker container
    iface.launch(server_name="0.0.0.0", server_port=7860)

