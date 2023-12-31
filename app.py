import json
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError

app = Flask(__name__)
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt3turbo', methods=['GET', 'POST'])
def gpt3turbo():
    user_input=request.args.get('user_input') if request.method=='GET' else request.form['user_input']
    messages=[{"role": "system", "content": user_input}]

    try:
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content=response.choices[0].message["content"]
    except RateLimitError:
        content="The server is currently experiencing high traffic. Please try again later."

    return jsonify(content=content)

if __name__=='__main__':
    app.run(debug=True)

