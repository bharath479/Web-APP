pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/bharath479/Web-APP.git'
      }
    }

    stage('Install Dependencies') {
      steps {
        sh 'npm install'
      }
    }

    stage('Run App') {
      steps {
        sh 'nohup npm start &'
      }
    }
  }

  post {
    always {
      echo 'Pipeline execution complete.'
    }
  }
}