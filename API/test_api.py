"""Test api to work with streaming data"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def display():
    data = request.get_json()
    print(jsonify(data))
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(port='9000', debug=True)

