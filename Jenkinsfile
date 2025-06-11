pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'github-token'
        SONARCLOUD_SERVER = 'SonarCloud'
        SONARCLOUD_URL = 'https://sonarcloud.io'
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

        stage('Verificar o crear proyecto en SonarCloud') {
            steps {
                withCredentials([string(credentialsId: 'sonarcloud-token', variable: 'SONAR_TOKEN')]) {
                    bat """
                        curl -s -u %SONAR_TOKEN%: %SONARCLOUD_URL%/api/projects/search?projects=%PROJECT_KEY% > result.json
                        findstr /C:"\"key\":\"%PROJECT_KEY%\"" result.json > nul
                        if errorlevel 1 (
                            echo Proyecto no existe. Creando...
                            curl -X POST -u %SONAR_TOKEN%: %SONARCLOUD_URL%/api/projects/create -d "name=%PROJECT_NAME%" -d "project=%PROJECT_KEY%" -d "organization=sonar-bhochoab"
                        ) else (
                            echo Proyecto ya existe en SonarCloud.
                        )
                    """
                }
            }
        }

        stage('Análisis SonarCloud') {
            steps {
                withSonarQubeEnv("${SONARCLOUD_SERVER}") {
                    withCredentials([string(credentialsId: 'sonarcloud-token', variable: 'SONAR_TOKEN')]) {
                        bat """
                            sonar-scanner ^
                            -Dsonar.projectKey=%PROJECT_KEY% ^
                            -Dsonar.organization=tu-organizacion ^
                            -Dsonar.sources=. ^
                            -Dsonar.language=py ^
                            -Dsonar.host.url=%SONARCLOUD_URL% ^
                            -Dsonar.login=%SONAR_TOKEN%
                        """
                    }
                }
            }
        }
    }
}
