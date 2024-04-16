from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message')
def index():
    return jsonify({"author": "rudimk", "text": "In remembrance of Earth's past."})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)