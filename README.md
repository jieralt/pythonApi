# pythonApi

python -V
Python 3.10.6

pip -V
pip 24.0 from C:\Users\Administrator\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)


pip install -r requirements.txt


git credential-cache exit
git config --global --unset credential.helper
git remote set-url origin https://jieralt@github.com/jieralt/pythonApi.git
git push origin main


linux
# 启动 supervisord
supervisord -c supervisord.conf

# 检查状态
supervisorctl -c supervisord.conf status

# 关闭 supervisord
supervisorctl -c supervisord.conf shutdown