pipeline {
    agent any

    environment {
        SONARQUBE_SERVER = 'BCH SonarQube-Server' // nombre configurado en Jenkins
        SCANNER_TOOL = 'SonarScanner'  // nombre del scanner configurado
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-token',
                    url: 'https://github.com/bhochoab/validador_urls.git',
                    branch: 'develop'
            }
        }

        stage('SonarQube Scan') {
    steps {
        withSonarQubeEnv("${SONARQUBE_SERVER}") {
            script {
                def scannerHome = tool name: "${SCANNER_TOOL}", type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                bat "${scannerHome}\\bin\\sonar-scanner.bat"
            }
        }
    }
}

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
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
