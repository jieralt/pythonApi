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




sudo useradd jenkins
<!-- sudo passwd jenkins -->
sudo mkdir -p /www/wwwroot/pythonApis
sudo chown -R jenkins:jenkins /www/wwwroot/pythonApis

sudo chmod -R 755 /www/wwwroot/pythonApis

sudo visudo
<!-- add -->

jenkins ALL=(ALL) NOPASSWD: ALL

sudo -u jenkins -i
echo '' | sudo -S cp -r . /www/wwwroot/pythonApis
sudo -i


linux
# 启动 supervisord
supervisord -c supervisord.conf

# 检查状态
supervisorctl -c supervisord.conf status

# 关闭 supervisord
supervisorctl -c supervisord.conf shutdown


# 赋予目录和文件足够的权限
sudo chown -R root:root /home/www/.jenkins/workspace/pythonApi
sudo chmod -R 755 /home/www/.jenkins/workspace/pythonApi

# 确保 supervisord 和相关日志文件有正确的权限
sudo touch /tmp/supervisord.log /var/log/flaskapp.err.log /var/log/flaskapp.out.log
sudo chown root:root /tmp/supervisord.log /var/log/flaskapp.err.log /var/log/flaskapp.out.log
sudo chmod 644 /tmp/supervisord.log /var/log/flaskapp.err.log /var/log/flaskapp.out.log
