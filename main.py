from flask import Flask, request, jsonify
from flask_cors import CORS
from services.ia_services import IAService

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    resposta = IAService.gerar_resposta(user_message)
    return jsonify({"response": resposta})

if __name__ == "__main__":
    app.run(debug=True)

