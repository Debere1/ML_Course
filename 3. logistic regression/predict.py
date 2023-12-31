# #### Load the data

import pickle
import sklearn
from flask import Flask
from flask import request
from flask import jsonify

model_data = 'model_C1.bin'

with open (model_data, 'rb') as f_in:
    dv, model = pickle.load( f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])

def predict ():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5

    result = {
        'churn probability': float(y_pred),
        'churn': bool(churn)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
