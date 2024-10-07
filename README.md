# HashiCorp-Vault-CI-CD-Pipeline



## Project Overview

This project demonstrates how to build a CI/CD pipeline using Jenkins, Vault for secret management, Flask as the web framework, Docker for containerization, and Nginx for reverse proxying. The app pulls AWS credentials securely from HashiCorp Vault and exposes a simple Flask web app.

## Prerequisites

- Jenkins, Vault, Docker installed on Ubuntu.
- Nginx installed for reverse proxying.
- Basic understanding of Jenkins, Flask, and Docker.

## Steps

1. **Set up Jenkins:**
   - Install Jenkins on your Ubuntu instance.
   - Set up credentials for Vault inside Jenkins.

2. **Configure Vault:**
   - Install and configure Vault.
   - Store your AWS credentials inside Vault.

3. **Flask Application:**
   - The Flask app retrieves AWS secrets from Vault and displays them on the web.

4. **Dockerize the App:**
   - Dockerize the Flask app for easy deployment.

5. **Nginx Configuration:**
   - Use Nginx to reverse proxy both Jenkins and Flask.

6. **CI/CD Pipeline:**
   - Create a `Jenkinsfile` that automates the entire process from code checkout to app deployment.
