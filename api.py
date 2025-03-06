from flask import Flask, request, jsonify
from flask_cors import CORS
from client import APIClient
from endpoints import APIEndpoints

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

client = APIClient(base_url="https://192.168.10.61", auth_token="your_auth_token")
api = APIEndpoints(client)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    response = api.login(data['username'], data['password'])
    return jsonify(response[0]["result"])

@app.route('/api/permissions', methods=['POST'])
def get_permissions():
    token = request.headers.get('X-Auth-Token')
    response = api.get_permissions({'X-Auth-Token': token})
    return jsonify(response)

@app.route('/api/browse', methods=['POST'])
def browse():
    data = request.json
    token = request.headers.get('X-Auth-Token')
    headers = {'X-Auth-Token': token}
    response = api.browse(data['var'], data['mode'], headers)
    return jsonify(response)

@app.route('/api/read', methods=['POST'])
def read():
    data = request.json
    token = request.headers.get('X-Auth-Token')
    headers = {'X-Auth-Token': token}
    response = api.read(data['var'], headers)
    return jsonify(response)

@app.route('/api/write', methods=['POST'])
def write():
    data = request.json
    token = request.headers.get('X-Auth-Token')
    headers = {'X-Auth-Token': token}
    response = api.write(data['var'], data['value'], headers)
    return jsonify(response)

@app.route('/api/ping', methods=['POST'])
def ping():
    token = request.headers.get('X-Auth-Token')
    response = api.ping({'X-Auth-Token': token})
    return jsonify(response)

@app.route('/api/logout', methods=['POST'])
def logout():
    token = request.headers.get('X-Auth-Token')
    response = api.logout({'X-Auth-Token': token})
    return jsonify(response)

@app.route('/api/write_speed', methods=['POST'])
def write_speed():
    data = request.json
    token = request.headers.get('X-Auth-Token')
    headers = {'X-Auth-Token': token}
    response = api.write_speed(data['var'], data['value'], headers)
    return jsonify(response)

@app.route('/api/turn_on', methods=['POST'])
def turn_on():
    token = request.headers.get('X-Auth-Token')
    headers = {'X-Auth-Token': token}
    response = api.turn_on(headers)
    return jsonify(response)

@app.route('/api/turn_off', methods=['POST'])
def turn_off():
    token = request.headers.get('X-Auth-Token')
    headers = {'X-Auth-Token': token}
    response = api.turn_off(headers)
    return jsonify(response)




if __name__ == '__main__':
    app.run(debug=True)