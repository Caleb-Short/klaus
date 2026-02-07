# klaus/app.py
import gradio as gr
from core.router import route_input

chat_history = []

def respond(message):
    chat_history.append({"role": "user", "content": message})
    response = route_input(message, chat_history)
    chat_history.append({"role": "assistant", "content": response})
    return chat_history, ""

with gr.Blocks(title="Klaus - Local AI") as demo:
    gr.Markdown("## Klaus — German Precision AI")
    chatbot = gr.Chatbot(label="Klaus", type="messages")
    msg = gr.Textbox(label="Ask Klaus...", placeholder="Type your question here")

    msg.submit(respond, inputs=msg, outputs=[chatbot, msg])

demo.launch()
