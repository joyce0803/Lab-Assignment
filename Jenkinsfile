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

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Project') {
            steps {
                script {
                    sh 'python model.py && python server.py'
                }
            }
        }

        stage('Test API') {
            steps {
                script {
                    sh 'python request.py'
                }
            }
        }
    }
}
