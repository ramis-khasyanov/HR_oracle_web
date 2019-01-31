from flask import Flask
from flask import request
import joblib
import pandas as pd
import json


app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    json_str = request.get_json()
    data = json.loads(json_str)
    X_test = pd.Series(data).values.reshape(1, -1)
    model = joblib.load('models/our_model.pkl')
    y_pred = model.predict_proba(X_test)
    return str(y_pred)


@app.route("/test_server", methods=["GET"])
def test_server():
    return 'Server is working well'


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)