pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                sh '''
                    . venv/bin/activate
                    python app.py
                '''
            }
        }
    }

    post {
        success {
            echo "######################## Build succeeded! ########################"
        }
        failure {
            echo "######################## Build failed! #######################"
        }
    }
}