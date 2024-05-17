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
                pip install --upgrade pip
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

        stage('Copy Files') {
            steps {
                sh '''
                echo '' | sudo -S cp -r . $PERSISTENT_PATH
                '''
            }
        }

        stage('Copy Virtual Environment and Run Flask App') {
            steps {
                sh '''
                sudo -S cp -r $VENV_PATH $PERSISTENT_PATH/$VENV_PATH
                cd $PERSISTENT_PATH
                sudo -u www bash -c '
                source $PERSISTENT_PATH/$VENV_PATH/bin/activate
                nohup python run.py > flaskapp.log 2>&1 &
                sleep 5
                cat flaskapp.log
                '
                '''
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
