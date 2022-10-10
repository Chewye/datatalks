import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}


response = requests.post(url, json=client).json()
print(response)


if response['churn'] == True:
    print('sending promo email to %s' %customer_id)
else:
    print('Not sending promo email to %s' %customer_id)