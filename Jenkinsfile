pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'
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
                        sh "kill -9 ${pids}"
                    }
                }
            }
        }

        stage('Run Flask App') {
            steps {
                script {
                    sh '''
                    source $VENV_PATH/bin/activate
                    nohup python run.py > flaskapp.log 2>&1 &
                    sleep 5
                    cat flaskapp.log
                    '''
                    // 检查应用是否运行
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
            cleanWs(notFailBuild: true, disableDeferredWipeout: true, deleteDirs: true)
        }
    }
}
