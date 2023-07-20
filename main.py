import gradio as gr
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'genAI FTW!!!!!!'

if __name__ == '__main__':
    app.run()


# def chatbot(conversation):
#     new_message = 'Hello World!'
#     return new_message
# if __name__ == "__main__":
#     with gr.Blocks() as demo:
#         chat = gr.Chatbot()
#         msg = gr.Textbox()
#         clear = gr.ClearButton([msg, chat])
