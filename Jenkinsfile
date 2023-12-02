pipeline {
    agent {dockerfile true}

    environment {
        DOCKER_IMAGE = 'joyce0803/lab_ass_flask_api:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/joyce0803/Lab-Assignment.git'
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).run('--rm -p 5000:5000')
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

    post {
        always {
            script {
                docker.image(DOCKER_IMAGE).stop()
            }
        }
    }
}
