pipeline {
    agent any

    stages {
        stage('Clone du dépôt') {
            steps {
                git 'https://github.com/eisenhowair/Modelisation3D.git'
            }
        }
        stage('Installation des dépendances') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                //sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Build et Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -p "test_*.py"'
            }
        }
    }
}