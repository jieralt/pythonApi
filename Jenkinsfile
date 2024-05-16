pipeline {
    agent any

    environment {
        // 设置虚拟环境路径
        VENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // 克隆 Git 仓库
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    // 安装虚拟环境
                    sh 'python3 -m venv ${VENV}'
                    // 激活虚拟环境并安装依赖
                    sh '. ${VENV}/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run Flask App') {
            steps {
                script {
                    // 运行 Flask 应用
                    sh '. ${VENV}/bin/activate && flask run'
                }
            }
        }
    }

    post {
        always {
            // 清理工作区
            cleanWs()
        }
    }
}
