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

        stage('Clean Target Directory') {
            steps {
                sh '''
                echo '' | sudo -S rm -rf $PERSISTENT_PATH
                echo '' | sudo -S mkdir -p $PERSISTENT_PATH
                '''
            }
        }

        stage('Copy Files to Target Directory') {
            steps {
                sh '''
                echo '' | sudo -S cp -r . $PERSISTENT_PATH
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                cd $PERSISTENT_PATH
                python3 -m venv $VENV_PATH
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd $PERSISTENT_PATH
                source $VENV_PATH/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
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
