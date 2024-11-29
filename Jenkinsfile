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
                        sh 'sudo SDL_VIDEODRIVER=$SDL_VIDEODRIVER python3 Mendelbrot.py'
                        sh 'sudo SDL_VIDEODRIVER=$SDL_VIDEODRIVER python3 Julia.py'
                        sh 'sudo SDL_VIDEODRIVER=$SDL_VIDEODRIVER python3 Koch.py'
                    }
                }
            }
        }
    }
}
