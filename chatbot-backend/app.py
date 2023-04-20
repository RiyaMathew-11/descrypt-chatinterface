from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    # Process the message and generate a response
    response = f"You said: {message}"
    print(response)
    return jsonify(response=response)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
