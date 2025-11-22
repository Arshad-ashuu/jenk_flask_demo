pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building the app....'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          docker.build('my_jenk_flask-image')
        }
      }
    }
  }
}
