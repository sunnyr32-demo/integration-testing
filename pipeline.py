pipeline {
  agent any
  
  stages {
    stage('Build') {
      steps {
        // Build the application
        sh 'mvn clean package'
      }
    }
    stage('Test') {
      steps {
        // Run integration tests against the API endpoint
        sh 'mvn test -Dtest=IntegrationTest'
      }
    }
  }
}
