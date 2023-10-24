# #### Load the data

import pickle
import sklearn

model_data = 'model_C1.bin'

with open (model_data, 'rb') as f_in:
    dv, model = pickle.load( f_in)

customer = {
    'customerid': '3454-jfubc',
    'gender':  'male',
    'seniorcitizen': 1,
    'partner': 'no',
    'dependents': 'no',
    'tenure': 68,
    'phoneservice': 'yes',
    'multiplelines': 'no',
    'internetservice': 'no',
    'onlinesecurity': 'no_internet_service',
    'onlinebackup': 'no_internet_service',
    'deviceprotection': 'no_internet_service',
    'techsupport': 'no_internet_service',
    'streamingtv':  'no_internet_service',
    'streamingmovies': 'no_internet_service',
    'contract': 'two_year',
    'paperlessbilling': 'yes',
    'paymentmethod': 'credit_card_(automatic)',
    'monthlycharges': 5.0,
    'totalcharges': 340.0,
    'churn':   0
}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0,1]

print('input', customer)
print('churn probability', y_pred)