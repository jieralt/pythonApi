from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, Namespace

api_bp = Blueprint('api', __name__)
api = Api(api_bp, doc='/swagger/')




ns = Namespace('main', description='Main operations')
api.add_namespace(ns)

@ns.route('/')
class HelloWorld(Resource):
    @ns.doc(params={'name': 'The name to welcome'})
    def get(self):
        '''Returns a welcome message'''
        name = request.args.get('name', 'Guest')
        return f"Hello, World! Welcome {name} !!!"

@ns.route('/welcome/<string:user>')
class WelcomeUser(Resource):
    @ns.doc(params={'user': 'The user to welcome'})
    def get(self, user):
        '''Returns a personalized welcome message'''
        return f"Hello, {user}! Welcome to our application!"
    
    
# @ns.route('/danmaku', methods=['POST'])
# def receive_danmaku():
#     data = request.get_json()
#     danmaku_content = data.get('danmaku')
#     print(f"Received in Flask: {danmaku_content}")
#     # 在这里可以处理接收到的弹幕数据，例如将其发送到Unity
#     return jsonify({"status": "success"}), 200

