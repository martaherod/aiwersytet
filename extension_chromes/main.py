#dotenv to rozszerzenie pythonowe, które służy do wczytania pliku .env do zmiennych środowiskowych
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

# tu tworzymy aplikacje
app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def convert_text():
    return jsonify({"text":"trololo"})

app.run(debug=True)
# jeśli w wersji deweloperskiej to możemy zostawić debug=true, bo od razu bedziemy widziec z zczego ewentualny błąd wynika