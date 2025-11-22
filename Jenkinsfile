pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/Arshad-ashuu/jenk_flask_demo.git'
      }
    }
    stage('Build') {
      steps {
        echo 'Building the app...'
      }
    }
  }
}
