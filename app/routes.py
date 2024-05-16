from flask import Blueprint, request

bp = Blueprint('main', __name__)

# @bp.route('/')
# def hello():
#     return "Hello, World!"

@bp.route('/')
def hello():
    name = request.args.get('name', 'Guest')
    return f"Hello, World! Welcome {name} !!!"
