from flask import Blueprint, jsonify, request
import os
import json

options_bp = Blueprint('options', __name__)
data_file = os.path.join('data', 'tasks.json')

# 初始化数据文件
if not os.path.exists(data_file):
    with open(data_file, 'w') as file:
        json.dump([], file)

@options_bp.route('/tasks', methods=['GET'])
def get_tasks():
    with open(data_file, 'r') as file:
        tasks = json.load(file)
    return jsonify(tasks)

@options_bp.route('/tasks', methods=['POST'])
def save_tasks():
    tasks = request.json
    with open(data_file, 'w') as file:
        json.dump(tasks, file)
    return jsonify({"status": "success"}), 200
