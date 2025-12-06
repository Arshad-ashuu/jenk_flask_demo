pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            // optional: args '-u root' if you need extra installs
        }
    }

    stages {

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -q
                '''
            }
        }

        stage('Run Flask App (Sanity Check)') {
            when {
                expression { return false } 
            }
            steps {
                sh '''
                    . venv/bin/activate
                    python app.py &
                    sleep 5
                    curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo "Build OK: Tests passed!"
        }
        failure {
            echo "Build FAILED. Check console log."
        }
    }
}
