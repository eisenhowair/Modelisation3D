pipeline {
    agent any

    environment {
        SDL_VIDEODRIVER = 'x11' // xhost +SI:localuser:jenkins (pour que jenkins puisse utiliser x11)
    }

    stages {
        stage('Build et Test') {
            steps {
                dir('TP1_marching_squares') {
                    sh 'python3 marching-squares.py'
                }
                dir('TP3_mendelbrot') {
                    // avec SDL_VIDEODRIVER
                    script {
                        withEnv(['SDL_VIDEODRIVER=x11']) {
                            sh 'python3 Mendelbrot.py'
                            sh 'python3 Julia.py'
                            sh 'python3 Koch.py'
                        }
                    }
                }
            }
        }
    }
}
