from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

VAULT_ADDR = os.getenv('VAULT_ADDR', 'http://127.0.0.1:8200')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')

def get_secret():
    if not VAULT_TOKEN:
        return "Vault Token not set!"
    
    headers = {'X-Vault-Token': VAULT_TOKEN}
    secret_url = f"{VAULT_ADDR}/v1/secret/data/myapp"
    response = requests.get(secret_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        aws_access_key = data['data']['data']['aws_access_key']
        aws_secret_key = data['data']['data']['aws_secret_key']
        return f"Access Key: {aws_access_key}, Secret Key: {aws_secret_key}"
    else:
        return "Failed to fetch secrets from Vault!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-secrets')
def fetch_secrets():
    secrets = get_secret()
    return render_template('secrets.html', secrets=secrets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
