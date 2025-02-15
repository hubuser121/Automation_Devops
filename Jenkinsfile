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
                script {
                    bat "docker build -t my-app:latest ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    bat "docker run -d -p 5000:5000 --name my-app-container my-app:latest"
                }
            }
        }

        stage('Check Running Containers') {
            steps {
                script {
                    bat "docker ps"
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    // Runs Python app inside the container (background mode)
                    bat "docker exec -d my-app-container python app.py"
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs!'
        }
    }
}
