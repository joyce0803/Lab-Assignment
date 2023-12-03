pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/joyce0803/Lab-Assignment.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t joyce0803/lab_ass_flask_api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 joyce0803/lab_ass_flask_api'
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
    }
}