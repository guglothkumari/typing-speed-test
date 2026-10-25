pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials-id'
        IMAGE_NAME = 'guglothkumari/typing-speed-test'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Builds the image and tags it
                    app = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                    app.tag("latest")
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        app.push("${IMAGE_TAG}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
                sh 'kubectl rollout restart deployment/typing-speed-test-deployment'
            }
        }
    }
}