# #### Load the data

import pickle
import sklearn
from flask import Flask

model_data = 'model_C1.bin'

with open (model_data, 'rb') as f_in:
    dv, model = pickle.load( f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])

def predict (customer):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    return y_pred

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
