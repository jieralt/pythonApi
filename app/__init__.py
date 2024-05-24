# from flask import Flask
# from .routes import bp as main_bp

# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(main_bp)

#     return app


import os
from flask import Flask, render_template
from .options_routes import options_bp
from .routes import api_bp

def create_app():
    # template_dir = os.path.abspath('templates')
    # app = Flask(__name__, template_folder=template_dir)
    app = Flask(__name__, template_folder='templates')
    # app = Flask(__name__)
    # app = Flask(__name__, static_folder='templates', template_folder='templates')
    # app = Flask(__name__, template_folder='templates')

    app.register_blueprint(api_bp, url_prefix='/api')  # 使用url_prefix注册蓝图
    app.register_blueprint(options_bp, url_prefix='/options')


    @app.route('/')
    def index():
        print("Current working directory:", os.getcwd())
        print("Template folder path:", os.path.join(os.getcwd(), 'templates'))
        return render_template('index.html')
    

    return app
