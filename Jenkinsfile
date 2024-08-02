pipeline {
    agent any
    environment {
        GITNAME = 'songminjjuk'
        GITMAIL = 'alstjrdlep@naver.com'
        GITWEBADD = 'https://github.com/songminjjuk/fast.git'
        GITSSHADD = 'git@github.com:songminjjuk/fast.git'
        GITCREDENTIAL = 'git_cre'
        DOCKERHUB = 'alstjrdlep/fast'
        DOCKERHUBCREDENTIAL = 'docker_cre'
    }
    
    stages{
        stage('Checkout Github') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [],
                userRemoteConfigs: [[credentialsId: GITCREDENTIAL, url: GITWEBADD]]])
            }
            post {
                failure {
                    sh "echo clone failed"
                }
                success {
                    sh "echo clone success"
                }
            }
        }
        stage('docker image build') {
            steps {
                sh "docker build -t ${DOCKERHUB}:${currentBuild.number} ."
                sh "docker build -t ${DOCKERHUB}:latest ."
                // currentBuild.number 젠킨스가 제공하는 빌드넘버 변수
                // oolralra/fast:<빌드넘버> 와 같은 이미지가 만들어질 예정
            }
            post {
                failure {
                    sh "echo image build failed"
                }
                success {
                    sh "echo image build success"
                }
            }
        }
    }
}