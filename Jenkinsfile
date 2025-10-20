pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                git(
                    branch: 'main',
                    url: 'https://github.com/ZiadAbillama/videostore'
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t videostore-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop videostore-app || exit 0'
                bat 'docker rm videostore-app || exit 0'
            }
        }

        stage('Run New Container') {
            steps {
                bat 'docker run -d --name videostore-app -p 8000:8000 videostore-app:latest'
            }
        }
    }
}
