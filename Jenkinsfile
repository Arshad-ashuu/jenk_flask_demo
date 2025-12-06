pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
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