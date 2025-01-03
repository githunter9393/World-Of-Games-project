

pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // Your DockerHub credentials in Jenkins
        IMAGE_NAME = 'your_dockerhub_username/WOG_image' // Docker image name
        CONTAINER_NAME = 'WOG_container' // Docker container name
        SELENIUM_IMAGE = 'selenium/testing-script' // in this case the testing script will run locally, outside of a container
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/githunter9393/World-Of-Games-project.git', branch: 'main' // Checkout your Python app repo
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'echo"TestUser:11" > test.txt'
                }
                sh 'docker build -t WOG_image .'
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Flask app in a Docker container on localhost
                    sh 'docker run -d -p 8777:8777 --name WOG_container WOG_image'

                    // wait for the app to start
                    sleep(time: 5, unit: 'SECONDS')
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Run the selenium python script and capture the exit code
                    def exitCode = sh(script: 'python3 tests/e2e.py', returnStatus: true)

                    // Check exit code (0 = success, 1 = failure)
                    if (exitCode != 0) {
                    error("Selenium test failed. Exiting pipeline")
                    }
                }
            }
        }

        stage('Terminate Docker Container') {
            steps {
                script {
                    // Stop and remove the Flask container
                    sh 'docker stop WOG_container'
                    sh 'docker rm WOG_container'
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Login to DockerHub
                    sh 'echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin'

                    // Push Docker image to DockerHub
                    sh 'docker push WOG_image'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up workspace and Docker containers if needed
                sh 'docker system prune -f'
            }
        }
    }
}
