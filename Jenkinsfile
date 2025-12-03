pipeline {
    agent any   // runs on any available Jenkins agent

        stages {
            stage('Checkout') {
                steps {
                git branch: 'main', url: 'https://github.com/Arshad-ashuu/jenk_flask_demo.git'
             }
            }

        stage('Build') {
            steps {
                echo '################ Building Python project... ####################'
                // Normally you'd install dependencies here
            }
        }

        stage('Test') {
            steps {
                echo '##################### Running Python script... ####################'
                sh 'python3 app.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}