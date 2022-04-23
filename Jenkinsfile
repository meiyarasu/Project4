node ('master') {
    stage('Checkout') {
        echo 'Shared stage'

        checkout scm
    }
    stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarTest';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }

}
