from flask import Flask, render_template, request, jsonify
import os
import openai

# Set up OpenAI API credentials
os.environ['OPENAI_API_KEY'] = "a4e7007a05654dcc97722d1671249ece"
os.environ['OPENAI_API_BASE'] = "https://htioaiservice.openai.azure.com/"
os.environ['OPENAI_API_VERSION'] = "2023-5-15"

openai.api_type = "azure"
openai.api_base = "https://htioaiservice.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
    response = openai.Completion.create(
        engine="restaurant",
        prompt=text,
        temperature=1,
        max_tokens=100,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None)
    return response.choices[0].text.strip()


if __name__ == '__main__':
    app.run()
