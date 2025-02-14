pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'hubuser121/tracking-devops:latest'
        REGISTRY_URL = 'docker.io/hubuser121'
        K8S_NAMESPACE = 'devops-tracking'
        KUBECONFIG_CREDENTIALS_ID = 'kubeconfig-secret'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/hubuser121/Automation_devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: KUBECONFIG_CREDENTIALS_ID]) {
                        sh 'kubectl apply -f config/k8s/deployment.yaml'
                        sh 'kubectl apply -f config/k8s/service.yaml'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh './automation-scripts/test-script.sh'
                }
            }
        }

        stage('Monitor with Prometheus') {
            steps {
                script {
                    sh 'kubectl apply -f config/prometheus.yml'
                }
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
