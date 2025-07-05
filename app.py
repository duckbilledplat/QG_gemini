from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

app = Flask(__name__)

def generate_quote(emotion):
    prompt = f"""You're an inspirational quote generator. A person says they are feeling "{emotion}".
Give them one short, motivational quote tailored to that emotion."""
    response = model.generate_content(prompt)
    return response.text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    quote = ""
    if request.method == "POST":
        feeling = request.form.get("feeling")
        quote = generate_quote(feeling)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
