from flask import Flask, render_template, request
import json
import urllib.request
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/getweather', methods=['POST', 'GET'])
def weather():
    if request.method =='POST':
        location = request.form['city']
    else:
        location = 'chennai'  
        api='5767f57045cd0338348797d4bb45ee87'
        try:
            source =urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+api).read()
            response_data = json.loads(source)
            data = {
                'country_code': str(response_data['sys']['country']),
                'temp': str(response_data['main']['temp']) + '°K', 
                'location': str(response_data["name"]),
            }
            return render_template('index.html', data=data)
        except (Exception):
            return render_template('index.html', 
            error="Give the correct location")
app.run(host='0.0.0.0', port=8080)
if __name__ == '__main__':
    app.run(debug=True)