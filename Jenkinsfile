pipeline {
    agent any

    environment {
        SONARQUBE_SERVER = 'POC-Sonar' // nuevo nombre configurado en Jenkins
        SCANNER_TOOL = 'SonarScanner'  // sigue siendo el scanner local
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'GITHUB-Token',
                    url: 'https://github.com/bhochoab/validador_urls.git',
                    branch: 'develop'
            }
        }

        stage('SonarCloud Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    script {
                        def scannerHome = tool name: "${SCANNER_TOOL}", type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                        bat "${scannerHome}\\bin\\sonar-scanner.bat"
                    }
                }
            }
        }
    }
    post {
        success {
            echo '✅ Análisis exitoso y Quality Gate aprobado.'
        }
        failure {
            echo '❌ Falló el análisis o el Quality Gate.'
        }
    }
}
