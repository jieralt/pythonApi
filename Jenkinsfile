pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'
        PERSISTENT_PATH = '/www/wwwroot/pythonApis'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv $VENV_PATH'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source $VENV_PATH/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Check and Stop Existing Flask App') {
            steps {
                script {
                    def pids = sh(script: "ps aux | grep 'python run.py' | grep -v grep | awk '{print \$2}'", returnStdout: true).trim()
                    if (pids) {
                        sh "echo '' | sudo -S kill -9 ${pids}"
                    }
                }
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                source $VENV_PATH/bin/activate
                echo '' | sudo -S cp -r . $PERSISTENT_PATH
                cd $PERSISTENT_PATH
                nohup python run.py > flaskapp.log 2>&1 &
                sleep 5
                cat flaskapp.log
                '''
                script {
                    def running = sh(script: "netstat -nl | grep ':8001 '", returnStatus: true) == 0
                    if (!running) {
                        error "Flask app is not running!"
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // 只清理 Jenkins 工作空间，不删除持久化目录中的文件
                sh 'rm -rf *'
            }
        }
    }
}
