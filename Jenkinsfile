pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/hubuser121/Automation_devops.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t my-app:latest .'
            }
        }
        stage('Run Container') {
            steps {
                script {
                    bat 'docker run -d -p 5000:5000 --name my-app-container my-app:latest'
                }
            }
        }
        stage('Check Running Containers') {
            steps {
                bat 'docker ps'
            }
        }
        stage('Run Application') {
            steps {
                script {
                    def status = bat(script: 'docker inspect -f "{{.State.Running}}" my-app-container', returnStdout: true).trim()
                    if (status != "true") {
                        bat 'docker logs my-app-container'
                        error "Container failed to start. Check logs."
                    }
                }
            }
        }
    }
}
