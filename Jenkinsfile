pipeline {
    agent any

    environment {
        IMAGE_NAME = 'arunkhrishna/arundockerimage'
    }

    stages {
        stage('Pull Code From GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/ArunKhrishna/kopsdeploymentv.git'
            }
        }

        stage('Build the Docker Image') {
            steps {
                script {
                    sh "sudo docker build -t arundockerimage ."
                    sh "sudo docker tag arundockerimage ${IMAGE_NAME}:latest"
                    sh "sudo docker tag arundockerimage ${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }

        stage('Push the Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh 'echo "$DOCKER_PASS" | sudo docker login -u "$DOCKER_USER" --password-stdin'
                    }
                    sh "sudo docker push ${IMAGE_NAME}:latest"
                    sh "sudo docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'sudo kubectl apply -f pod.yaml'
                    sh 'sudo kubectl rollout restart deployment loadbalancer-pod || true'
                }
            }
        }
    }
}
