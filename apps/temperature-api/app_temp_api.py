from flask import Flask, jsonify, request
import random

app = Flask(__name__)

#Маршрут /temperature?location=location#

@app.route('/temperature', methods=['GET'])
def get_temperature():
    location = request.args.get('location', '')
    sensor_id = request.args.get('sensor', '')


#Определяем локацию по ID температурного датчика#
    if not location:
        location = {
            "1": "Living Room",
            "2": "Bedroom",
            "3": "Kitchen"
        }.get(sensor_id, "Unknown")

#Определяем ID датчика по локации#
    if not sensor_id:
        sensor_id = {
            "Living Room": "1",
            "Bedroom": "2",
            "Kitchen": "3"
        }.get(location, "0")

    temperature = round(random.uniform(17.0, 29.0),2)

    return jsonify({
        "location": location,
        "sensor_id": sensor_id,
        "temperature": temperature
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
