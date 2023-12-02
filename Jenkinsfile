pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'joyce0803/lab_ass_flask_api:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[credentialsId: '9a43752f-e2de-40b6-9037-543caf420f0b', url: 'https://github.com/joyce0803/Lab-Assignment.git']]])
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container
                    docker.image(DOCKER_IMAGE).run('-p 5000:5000', '--rm')
                }
            }
        }

        stage('Test API') {
            steps {
                script {
                    // Execute script to test API
                    sh 'python request.py'
                }
            }
        }
    }

    post {
        always {
            script {
                // Stop Docker container
                docker.image(DOCKER_IMAGE).stop()
            }
        }
    }
}
