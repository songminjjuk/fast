pipeline {
    agent any
    environment {
        GITNAME = 'songminjjuk'
        GITMAIL = 'alstjrdlep@naver.com'
        GITWEBADD = 'https://github.com/songminjjuk/fast.git'
        GITSSHADD = 'git@github.com:songminjjuk/deployment.git'
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
        stage('docker image push') {
            steps {
                 withDockerRegistry(credentialsId: DOCKERHUBCREDENTIAL, url: '') {
                    sh "docker push ${DOCKERHUB}:${currentBuild.number}"
                    sh "docker push ${DOCKERHUB}:latest"
                }
            }
            post {
                failure {
                    sh "docker image rm -f ${DOCKERHUB}:${currentBuild.number}"
                    sh "docker image rm -f ${DOCKERHUB}:latest"
                    sh "echo push failed"
                }
                success {
                    sh "echo push success"
                }
             }
        }
        stage('Git Deployment update manifest file') {
            steps {
                git credentialsId: GITCREDENTIAL, url: GITSSHADD, branch: 'main'
                sh "git config --global user.email ${GITMAIL}"
                sh "git config --global user.name ${GITNAME}"
                sh "sed -i 's@${DOCKERHUB}:.*@${DOCKERHUB}:${currentBuild.number}@g' fast.yaml"
                
                sh "git add ."
                sh "git branch -M main"
                sh "git commit -m 'fixed tag ${currentBuild.number}'"
                sh "git remote remove origin"
                sh "git remote add origin ${GITSSHADD}"
                sh "git push origin main"
            }
            post {
                failure {
                    sh "echo update manifest failed"
                }
                success {
                    sh "echo update manifest success"
                }
            }
        }
    }
}