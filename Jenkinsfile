pipeline {
    agent any

    environment {
        VAULT_ADDR = 'http://127.0.0.1:8200'
        VAULT_TOKEN = credentials('vault-token')  // Jenkins credential holding the Vault token
    }

    stages {
        stage('Clone Repo') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/abdulbasit17/HashiCorp-Vault-CI-CD-Pipeline.git'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Retrieve Secrets from Vault') {
            steps {
                script {
                    withVault([vaultSecrets: [[path: 'secret/myapp', secretValues: [
                        [envVar: 'AWS_ACCESS_KEY', vaultKey: 'aws_access_key'],
                        [envVar: 'AWS_SECRET_KEY', vaultKey: 'aws_secret_key']
                    ]]]]) {
                        echo "AWS Access Key: ${AWS_ACCESS_KEY}"
                    }
                }
            }
        }
        stage('Cleanup Existing Docker Container') {
            steps {
                script {
                    sh '''
                    if [ "$(docker ps -q -f name=flask-container)" ]; then
                        docker stop flask-container
                        docker rm flask-container
                    fi
                    '''
                }
            }
        }
        stage('Run Flask App') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    flask run --host=0.0.0.0 --port=5000 &  # Runs Flask in the background
                    '''
                }
            }
        }
        stage('Docker Build and Run') {
            steps {
                script {
                    sh '''
                    docker build -t flask-app .
                    docker run -d -p 5000:5000 --name flask-container flask-app
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                // Optionally clean up Docker images after running
                sh 'docker system prune -f'
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
