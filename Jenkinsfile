pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                echo 'Dang build Docker Image...'
                sh 'docker build -t my-flask-app:latest .'
            }
        }
        stage('Deploy Container') {
            steps {
                echo 'Dang xoa container cu (neu co) va chay container moi...'
                sh 'docker stop flask-web || true'
                sh 'docker rm flask-web || true'
                sh 'docker run -d -p 5000:5000 --name flask-web my-flask-app:latest'
            }
        }
    }
}