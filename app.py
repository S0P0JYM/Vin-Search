from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    vin_info = None
    if request.method == 'POST':
        vin = request.form['vin']
        response = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodeVinValues/{vin}?format=json')
        vin_info = response.json()
    return render_template('index.html', vin_info=vin_info)

if __name__ == '__main__':
    app.run(debug=True)