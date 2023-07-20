import gradio as gr
def chatbot(conversation):
    new_message = 'Hello World!'
    return new_message
if __name__ == "__main__":
    with gr.Blocks() as demo:
        chat = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chat])
