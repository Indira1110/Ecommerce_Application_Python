pipeline {
    agent any

    environment {
        PYTHON_ENV = '.venv'
    }

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv .venv'
                sh './.venv/bin/python -m pip install --upgrade pip'
                sh './.venv/bin/python -m pip install -r requirements.txt'
                sh './.venv/bin/python -m playwright install chromium'
            }
        }

        stage('Test') {
            steps {
                sh './.venv/bin/python -m pytest -q --junitxml=pytest-report.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'pytest-report.xml'
        }
    }
}
