pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    sh 'python3 -m venv ${VENV}'
                    sh '. ${VENV}/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Check and Stop Existing Flask App') {
            steps {
                script {
                    // 检查是否有已运行的 Flask 应用，如果有则停止它
                    sh '''
                    pids=$(ps aux | grep "python run.py" | grep -v grep | awk '{print $2}')
                    if [ ! -z "$pids" ]; then
                        echo "Stopping existing Flask app..."
                        kill -9 $pids
                    fi
                    '''
                }
            }
        }
        stage('Run Flask App') {
            steps {
                script {
                    // 后台运行 Flask 应用，并将输出重定向到日志文件
                    sh '''
                    . ${VENV}/bin/activate
                    nohup python run.py > flaskapp.log 2>&1 &
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                // 输出 Flask 应用日志文件以帮助调试
                sh 'cat flaskapp.log || true'
                cleanWs()
            }
        }
    }
}
