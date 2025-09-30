from flask import Flask, request, jsonify
from chat_interface import get_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    return jsonify({"response": get_response(user_input)})

if __name__ == "__main__":
    app.run(debug=True)
