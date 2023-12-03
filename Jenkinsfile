pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[credentialsId: '9a43752f-e2de-40b6-9037-543caf420f0b', url: 'https://github.com/joyce0803/Lab-Assignment.git']]])
            }
        }

        stage('Pull Image') {
            steps {
                echo 'Pulling the image...'
                script {
                    env.IMAGE_ID = sh(script: 'docker pull joyce0803/lab_ass_flask_api:latest', returnStdout: true).trim()
                }
            }
        }


        stage('Run Image') {
            steps {
                echo 'Running the image...'
                script {
                    env.CONTAINER_ID = sh(script: 'docker run -d -p 8086:5000 joyce0803/lab_ass_flask_api:latest', returnStdout: true).trim()
                }
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    # Use the provided test script
                    python request.py
                '''
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                script {
                    sh 'docker stop ${CONTAINER_ID}'
                    sh 'docker rm ${CONTAINER_ID}'
                }
            }
        }
    }
}