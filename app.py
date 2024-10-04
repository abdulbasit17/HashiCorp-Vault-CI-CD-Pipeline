from flask import Flask
import hvac  # Import hvac for Vault

app = Flask(__name__)

# Function to retrieve secrets from Vault
def get_vault_secrets():
    client = hvac.Client(url='http://127.0.0.1:8200')  # Vault address
    client.token = 'hvs.87vSa12zTNEAXBa1nGGM4RkQ'  # Set your Vault token

    # Fetch the secret stored under 'secret/data/myapp'
    secret = client.secrets.kv.v2.read_secret_version(path='myapp')

    aws_access_key = secret['data']['data']['aws_access_key']
    aws_secret_key = secret['data']['data']['aws_secret_key']

    return aws_access_key, aws_secret_key

@app.route('/')
def home():
    aws_access_key, aws_secret_key = get_vault_secrets()
    return f"Access Key: {aws_access_key}, Secret Key: {aws_secret_key}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Ensure it runs on port 5000
