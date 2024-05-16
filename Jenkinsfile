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
                    // sh 'pip install supervisor'
                }
            }
        }
        stage('Run Flask App') {
            steps {
                script {
                    // 启动 Flask 应用程序
                    sh '. ${VENV}/bin/activate && supervisord -c ${SUPERVISORD_CONF}'
                }
            }
        }
    }

    post {
        always {
            script {
                // 停止 Flask 应用程序
                sh '. ${VENV}/bin/activate && supervisorctl -c ${SUPERVISORD_CONF} shutdown'
                cleanWs()
            }
        }
    }
}
