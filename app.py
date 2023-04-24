from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key ="c4422e8bfaa0fe2c56a3d8deb9c23d34"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather')
def weather():
    location = request.args.get('location')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    temperature = response['main']['temp']
    return f'The temperature in {location} is {temperature} degrees Celsius.'

if __name__ == '__main__':
    app.run(debug=True)
