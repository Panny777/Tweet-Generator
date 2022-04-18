import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        tweet = request.form["tweet"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_prompt(tweet),
            temperature=0.6,
            max_tokens=100
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(tweet):
    return """generate a tweet about.
""" + tweet
