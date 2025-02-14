pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hubuser121/Automation_devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t my-app:latest .'
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                bat 'docker push my-app:latest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'cmd /c run-tests.bat'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}

