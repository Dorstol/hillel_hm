import csv

import faker
import requests

from flask import Flask, request
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

fake = faker.Faker('uk_UA')
app = Flask(__name__)


@app.route("/generate_students")
@use_kwargs(
    {
        "count": fields.Int(
            validate=[validate.Range(max=1000)]
        ),
    },
    location='query'
)
def generate_students(count):
    """
    Generate students and save them to csv file
    return: csv file with students data
    """
    count = request.args.get('count')
    count = int(count)
    students = []
    for i in range(count):
        students.append(
            {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.ascii_free_email(),
                'password': fake.password(length=12),
                'birthday': fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=40),
            }
        )
    with open('students.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    return {'students': students}


@app.route("/bitcoin_price")
def get_bitcoin_value():
    """
    Get the current bitcoin price from the API
    return: price in selected currency
    """
    currency = request.args.get('currency', 'USD')
    count = request.args.get('count', '1')
    count = int(count)
    data = requests.get('https://bitpay.com/api/rates').json()
    get_currency_symbol = requests.get('https://bitpay.com/currencies').json()['data']

    # find currency symbol by currency name
    for i in range(len(get_currency_symbol)):
        if get_currency_symbol[i]['code'] == currency:
            currency_symbol = get_currency_symbol[i]['symbol']
            break

    # find price by currency name and return currency price and symbols
    for i in range(len(data)):
        if data[i]['code'] == currency:
            return {
                'price': str(data[i]['rate']) + currency_symbol,
                'converted price': str(round(count / data[i]['rate'], 2)) + get_currency_symbol[0]['symbol']
                    }


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
