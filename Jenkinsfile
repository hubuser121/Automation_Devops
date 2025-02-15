pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my-app:latest"
        REGISTRY = "docker.io/hubuser121"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hubuser121/Automation_devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh 'docker tag $DOCKER_IMAGE $REGISTRY/$DOCKER_IMAGE'
                    sh 'docker push $REGISTRY/$DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }

    post {
        failure {
            echo "❌ Pipeline failed. Check logs!"
        }
        success {
            echo "✅ Deployment successful!"
        }
    }
}
