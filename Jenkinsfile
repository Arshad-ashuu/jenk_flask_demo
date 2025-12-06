pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    sudo apt install -y python3 python3-pip python3-venv
                    python3 -m venv venv
                    . venv/bin/activate           
                    pip install -r requirements.txt
                '''
                echo "######################## pip install done ########################"
            }
        }

        stage('Run Python Script') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 app.py
                '''
                echo "######################## apppy runnning ########################"
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