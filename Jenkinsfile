pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'github-token'
        SONARQUBE_SERVER = 'SonarQube-Server'
        SONAR_HOST_URL = 'http://sonarqube.bch.bancodechile.cl:9002'
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

        stage('Verificar o crear proyecto en SonarQube') {
            steps {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                    bat """
                        curl -s -u %SONAR_TOKEN%: %SONAR_HOST_URL%/api/projects/search?projects=%PROJECT_KEY% > result.json
                        findstr /C:"\"key\":\"%PROJECT_KEY%\"" result.json > nul
                        if errorlevel 1 (
                            echo Proyecto no existe. Creando...
                            curl -X POST -u %SONAR_TOKEN%: %SONAR_HOST_URL%/api/projects/create -d "name=%PROJECT_NAME%" -d "project=%PROJECT_KEY%"
                        ) else (
                            echo Proyecto ya existe en SonarQube.
                        )
                    """
                }
            }
        }

        stage('Análisis SonarQube') {
            steps {
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                        bat """
                            sonar-scanner ^
                            -Dsonar.projectKey=%PROJECT_KEY% ^
                            -Dsonar.projectName=%PROJECT_NAME% ^
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
