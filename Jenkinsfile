pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'github-token'
        SONARQUBE_SERVER = 'SonarQube-Server'
        SONARQUBE_URL = 'http://sonarqube.bch.bancodechile.cl:9002'
        PROJECT_KEY = 'mi-proyecto-python'
        PROJECT_NAME = 'Mi Proyecto Python'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: "${GITHUB_CREDENTIALS}",
                    url: 'https://github.com/bhochoab/validador_urls.git',
                    branch: 'main'
            }
        }

        stage('Verificar proyecto en SonarQube') {
            steps {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                    bat """
                        echo Verificando si el proyecto existe en SonarQube...
                        curl -s -H "Authorization: Bearer %SONAR_TOKEN%" "%SONARQUBE_URL%/api/projects/search?projects=%PROJECT_KEY%" > result.json
                        findstr /C:"\"key\":\"%PROJECT_KEY%\"" result.json > nul
                        if errorlevel 1 (
                            echo Proyecto NO existe en SonarQube. Debe crearse manualmente.
                        ) else (
                            echo Proyecto ya existe en SonarQube.
                        )
                        del result.json
                    """
                }
            }
        }

        stage('Analizar con SonarQube') {
            steps {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                    withSonarQubeEnv("${SONARQUBE_SERVER}") {
                        bat """
                            sonar-scanner ^
                            -Dsonar.projectKey=%PROJECT_KEY% ^
                            -Dsonar.projectName="%PROJECT_NAME%" ^
                            -Dsonar.sources=. ^
                            -Dsonar.language=py ^
                            -Dsonar.login=%SONAR_TOKEN%
                        """
                    }
                }
            }
        }
    }
}
