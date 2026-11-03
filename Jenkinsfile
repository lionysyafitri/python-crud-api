pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Mengambil kode terbaru dari repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Membuat Docker image untuk aplikasi Flask...'
                sh 'docker build -t python-crud-api:manual .'
            }
        }

        stage('Deploy / Run Container') {
            steps {
                echo 'Menjalankan container Docker...'
                // Hapus container lama jika ada, lalu jalankan yang baru
                sh 'docker rm -f production-api-container || true'
                sh 'docker run -d --name production-api-container -p 5000:5000 -v production-api-data:/var/lib/backend_data python-crud-api:manual'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Memeriksa kesehatan endpoint API...'
                sh 'curl.exe -i http://localhost:5000/health || true'
            }
        }
    }

    post {
        success {
            echo 'Pipeline CI/CD Berhasil Dijalankan!'
        }
        failure {
            echo 'Pipeline CI/CD Gagal, silakan periksa log.'
        }
    }
}