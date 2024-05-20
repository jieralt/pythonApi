# from flask import Blueprint, request, Flask, jsonify



# app = Blueprint('main', __name__)

# # @bp.route('/')
# # def hello():
# #     return "Hello, World!"

# @app.route('/')
# def hello():
#     name = request.args.get('name', 'Guest')
#     return f"Hello, World! Welcome {name} !!!"

# @app.route('/welcome/<user>')
# def welcome(user):
#     return f"Hello, {user}! Welcome to our application!"


from flask import Blueprint, request
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

