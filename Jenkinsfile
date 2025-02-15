pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        docker.build('my-app:latest', 'docker')
                    } catch (Exception e) {
                        error "Failed to build Docker image: ${e.message}"
                    }
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    // Add steps to push Docker image to registry
                }
            }
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Add steps to run tests
                }
            }
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
