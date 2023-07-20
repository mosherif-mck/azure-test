from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/'):
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def hello():
    text = request.form['text']
    return f"genAI FTW{text}!!!!!!"

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
