
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Clinic Appointment project checked out from GitHub.'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python --version'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Validate Application') {
            steps {
                bat 'python -m py_compile app.py'
                echo 'Python syntax validation passed.'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker --version'
                bat 'docker build -t clinic-appointment .'
            }
        }
    }

    post {
        success {
            echo 'Clinic Appointment Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output for details.'
        }
    }
}
