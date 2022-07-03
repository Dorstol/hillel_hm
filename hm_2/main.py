import string
import pandas
from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def generate_password():
    """
    Generates a random password
    from 10 to 25 chars long
    with at least one digit,
    one uppercase letter,
    lowercase letter
    and one special character
    :return: random password
    """
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(characters)
    password = []
    for i in range(random.randint(10, 25)):
        password.append(random.choice(characters))
    if not any(char.isdigit() for char in password):
        password.append(random.choice(string.digits))
    if not any(char.isupper() for char in password):
        password.append(random.choice(string.ascii_uppercase))
    if not any(char.islower() for char in password):
        password.append(random.choice(string.ascii_lowercase))
    if not any(char in string.punctuation for char in password):
        password.append(random.choice(string.punctuation))
    password = "".join(password)
    return f'<b>{password}</b>'


@app.route("/average")
def calculate_average():
    """
    Calculates the average height and weight
    :return: average height and weight
    """
    data = pandas.read_csv('hw.csv')
    average = data.mean()
    return f'<b>average-height: {round(average[" Height(Inches)"], 2)}</b>\n' \
           f'<br><b>average-weight: {round(average[" Weight(Pounds)"], 2)}</b>'


app.run(host='localhost', port=8080, debug=True)
