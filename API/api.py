from flask import Flask, jsonify, request
import numpy as np
import pickle

rfc = pickle.load(open("iris_rfc.pkl", "rb"))

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def predict():
    # get json
    data = request.get_json(force=True)

    # convert the json into a numpy array
    predict_request = [data['sl'], data['sw'], data['pl'], data['pw']]
    predict_request = np.array(predict_request)

    # input: np_array, output: prediction result
    result = rfc.predict([predict_request])

    # return the prediction
    output = result[0]

    return jsonify(output.tolist())


if __name__ == '__main__':
    app.run(port='9000', debug=True)




