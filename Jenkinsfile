
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Project checked out from GitHub.'
            }
        }

        stage('Check Environment') {
            steps {
                sh 'java -version'
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Validate Application') {
            steps {
                sh 'python3 -m py_compile app.py'
                echo 'Python syntax validation passed.'
            }
        }
    }

    post {
        success {
            echo 'Clinic Appointment CI Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
