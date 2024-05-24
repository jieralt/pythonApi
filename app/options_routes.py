from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, Namespace
import os
import json

# 初始化 Blueprint
options_bp = Blueprint('options', __name__)
api = Api(options_bp, doc='/swagger/')

# 定义 Namespace
ns = Namespace('tasks', description='Task operations')
api.add_namespace(ns)

# 数据文件路径
data_file = os.path.join('data', 'tasks.txt')

# 初始化数据文件
if not os.path.exists(data_file):
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    with open(data_file, 'w') as file:
        json.dump([], file)

@ns.route('/')
class TaskList(Resource):
    def get(self):
        '''返回所有任务'''
        with open(data_file, 'r') as file:
            tasks = json.load(file)
        return jsonify(tasks)

    def post(self):
        '''保存所有任务'''
        tasks = request.json
        with open(data_file, 'w') as file:
            json.dump(tasks, file)
        return jsonify({"status": "success"}), 200
