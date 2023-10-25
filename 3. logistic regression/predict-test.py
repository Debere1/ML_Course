
import requests

url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
customer = {
    "customerid": "3454-jfubc",
    "gender":  "male",
    "seniorcitizen": 1,
    "partner": "no",
    "dependents": "no",
    "tenure": (68/12),
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "no",
    "onlinesecurity": "no_internet_service",
    "onlinebackup": "no_internet_service",
    "deviceprotection": "no_internet_service",
    "techsupport": "no_internet_service",
    "streamingtv":  "no_internet_service",
    "streamingmovies": "no_internet_service",
    "contract": "two_year",
    "paperlessbilling": "yes",
    "paymentmethod": "credit_card_(automatic)",
    "monthlycharges": (5 * 5.0),
    "totalcharges": (5 * 340.0/12),
    "churn":   0
}


response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('send promotional email to %s' %customer_id)
else:
    print('no send promotional email to %s' %customer_id)
