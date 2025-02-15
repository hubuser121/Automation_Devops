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
    }
}
