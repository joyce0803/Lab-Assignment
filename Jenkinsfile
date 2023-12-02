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
                    // Use the correct path to the 'pip' executable for Windows
                    def pipCmd = isUnix() ? 'pip' : 'C:\\Users\\jerri\\PycharmProjects\\Joyce Lab Assignment\\venv\\Scripts\\pip.exe'
                    bat "${pipCmd} install -r requirements.txt"
                }
            }
        }

        stage('Run Project') {
            steps {
                script {
                    bat 'python model.py && python server.py'
                }
            }
        }

        stage('Test API') {
            steps {
                script {
                    bat 'python request.py'
                }
            }
        }
    }
}
