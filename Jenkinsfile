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
                    docker.image(DOCKER_IMAGE).run("-d -p 8086:5000",'--rm')
                }
            }
        }

        stage('Test API') {
            steps {
                script {
                    sleep time: 10, unit: 'SECONDS' // Add a delay of 30 seconds (adjust as needed)
                    bat 'python request.py'
                }
            }
        }


        stage('Declarative: Post Actions') {
            steps {
                script {
                    // Stop the Docker container using the 'stop' command
                    sh "docker stop <899f85580ff7>"
                }
            }
        }

    }
}
