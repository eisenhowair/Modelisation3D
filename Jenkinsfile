pipeline {
    agent any

    stages {
        stage('Installation des dépendances') {
            steps {
                dir('Reconstruction3D') {
                    sh 'python3 -m pip install --upgrade pip'
                    //sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Build et Test') {
            steps {
                dir('TP1_marching_squares') {
                    sh 'python3 marching-squares.py'
                }
                dir('TP3_mendelbrot') {
                    sh 'python3 Mendelbrot.py'
                    sh 'python3 Julia.py'
                    sh 'python3 Koch.py'
                }
            }
        }
    }
}