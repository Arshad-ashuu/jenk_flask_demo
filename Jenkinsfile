pipeline {
    agent any   // run on any available Jenkins agent

    stages {
        stage('Checkout') {
            steps {
                // Jenkins will automatically check out SCM if configured,
                // but this makes it explicit.
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Use a virtual environment so dependencies are isolated.
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
            echo "######################## Build succeeded! Python script ran successfully.#################################"
        }
        failure {
            echo "######################## Build failed. Check logs for errors.########################"
        }
    }
}
