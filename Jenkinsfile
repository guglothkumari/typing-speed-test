
pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials-id'
        IMAGE_NAME = 'guglothkumari/typing-speed-test'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'python -m pip install -r requirements.txt'

                echo 'Running Flask application test cases...'
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def app = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                    app.tag("latest")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry(
                        'https://index.docker.io/v1/',
                        "${DOCKERHUB_CREDENTIALS}"
                    ) {
                        def app = docker.image("${IMAGE_NAME}:${IMAGE_TAG}")
                        app.push()

                        docker.image("${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
                bat 'kubectl rollout restart deployment/typing-speed-test-deployment'
                bat 'kubectl rollout status deployment/typing-speed-test-deployment --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
    }
}
