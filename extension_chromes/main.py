from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import OpenAI

load_dotenv()

app = Flask(__name__)


def summarize(text: str) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": "I will write you the text I gather from the webisite. I need you to make a summary of this text. Your response should contain only the summarized text in polish."
            }, {
                "role": "user",
                "content": text
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


@app.route('/summarize', methods=['POST'])
def convert_text():
    data = request.json
    longer_text = data.get('text', '')

    return jsonify({"text": summarize(longer_text)})


app.run(debug=True)
# Uruchamiam moje api: flask --app main run
# Zatrzymanie programu -> ctrl + c  (2 razy)
