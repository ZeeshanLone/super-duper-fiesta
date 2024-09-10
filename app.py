from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/api/echo', methods=['POST'])
def echo():
    # Get the JSON data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Return the received data as JSON
    return jsonify(data), 200

if __name__ == '__main__':
    # For production testing, use a WSGI server like Gunicorn
    # gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(host='0.0.0.0', port=5000)
