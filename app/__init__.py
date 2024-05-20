# from flask import Flask
# from .routes import bp as main_bp

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(main_bp)

#     return app


from flask import Flask
from .routes import api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/api')  # 使用url_prefix注册蓝图
    return app
