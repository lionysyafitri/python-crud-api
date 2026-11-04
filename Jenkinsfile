
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Mengambil source code dari repository GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Membuat Docker image Python REST API...'
                sh 'docker build -t python-crud-api:manual .'
            }
        }

        stage('Automated Testing') {
            steps {
                echo 'Menjalankan automated test di dalam Docker...'
                sh 'docker run --rm python-crud-api:manual python -m unittest -v test_app.py'
            }
        }

        stage('Deploy / Run Container') {
            steps {
                echo 'Menjalankan container Docker...'

                sh '''
                    docker rm -f production-api-container || true

                    docker run -d \
                        --name production-api-container \
                        -p 5000:5000 \
                        -v production-api-data:/var/lib/backend_data \
                        python-crud-api:manual
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Memeriksa kesehatan endpoint API...'

                sh '''
                    for i in $(seq 1 15); do
                        if curl -fsS http://host.docker.internal:5000/health; then
                            echo "API berhasil berjalan!"
                            exit 0
                        fi

                        sleep 2
                    done

                    echo "Health check gagal!"
                    exit 1
                '''
            }
        }
    }
}
