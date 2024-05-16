pipeline {
    agent any

    environment {
        VENV = "${WORKSPACE}/venv"
        SUPERVISORD_CONF = "${WORKSPACE}/supervisord.conf"
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
                    sh '. ${VENV}/bin/activate && pip install supervisor'
                }
            }
        }
        stage('Run Flask App') {
            steps {
                script {
                    sh '. ${VENV}/bin/activate && supervisord -c ${SUPERVISORD_CONF}'
                }
            }
        }
    }

    post {
        always {
            script {
                // 输出 supervisord 日志文件以帮助调试
                sh 'cat /tmp/supervisord.log || true'
                sh 'cat /var/log/flaskapp.err.log || true'
                sh 'cat /var/log/flaskapp.out.log || true'
                // 尝试停止 Flask 应用程序
                sh '. ${VENV}/bin/activate && supervisorctl -c ${SUPERVISORD_CONF} shutdown || true'
                cleanWs()
            }
        }
    }
}
