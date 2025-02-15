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
                    // Stop and remove any existing container
                    bat "docker rm -f my-app-container || echo 'No existing container to remove'"
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
