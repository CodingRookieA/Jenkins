pipeline {
    agent any

    stages {

        stage('Debug workspace') {
            steps {
                sh '''
                pwd
                ls -la
                '''
            }
        }

        stage('Setup Python venv') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirement.txt
                '''
            }
        }


        stage('Lint') {
            steps {
                sh '''
                . venv/bin/activate
                flake8 app/
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PWD
                pytest
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}