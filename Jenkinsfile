node ('master') {
    stage('Checkout') {
        echo 'Shared stage'

        checkout scm
    }
    stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }

}
