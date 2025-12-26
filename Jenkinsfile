pipeline {
    agent any

    stages {

        stage('Pending Notification') {
            steps {
                githubNotify context: 'CI',
                             status: 'PENDING',
                             description: 'Build queued...'
            }
        }

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
            echo 'Build good!'
            githubNotify context: 'CI', status: 'SUCCESS', description: 'Build passed!'
        }
        failure {
            echo 'Build bad!'
            githubNotify context: 'CI', status: 'FAILURE', description: 'Build failed!'
        }
    }
}