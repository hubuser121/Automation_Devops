pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hubuser121/my-app:latest"
        DOCKER_HUB_CREDENTIALS = "docker-hub-credentials"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hubuser121/Automation_devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    withDockerRegistry([credentialsId: DOCKER_HUB_CREDENTIALS, url: 'https://index.docker.io/v1/']) {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f k8s-deployment.yaml"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh "pytest tests/"
                }
            }
        }

        stage('Monitor with Prometheus') {
            steps {
                script {
                    sh "kubectl apply -f prometheus-config.yaml"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs!"
        }
    }
}
