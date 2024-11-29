from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Proxy endpoint
@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    # Extract the target URL and data from the request
    target_url = 'https://azure-openai-chat-eyb9fugmhahehmcp.canadacentral-01.azurewebsites.net/api/data'
    
    # Forward the request to the target API
    if request.method == 'GET':
        response = requests.get(target_url, params=request.args)
    elif request.method == 'POST':
        response = requests.post(target_url, json=request.json)
    
    # Return the response back to the client
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
