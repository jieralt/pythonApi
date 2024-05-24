from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, Namespace
import os

options_bp = Blueprint('options', __name__)
api = Api(options_bp, doc='/swagger/')

ns = Namespace('options', description='Options related operations')
api.add_namespace(ns)

data_file = os.path.join('data', 'selected_options.txt')

@ns.route('/submit-options')
class SubmitOptions(Resource):
    @ns.doc(params={'options': 'A list of selected options'})
    def post(self):
        '''Submits the selected options and saves them to a txt file'''
        data = request.json
        selected_options = data.get('options', [])
        with open(data_file, 'a') as file:
            for option in selected_options:
                file.write(option + '\n')
        return jsonify({'status': 'success', 'selected_options': selected_options})

@ns.route('/get-options')
class GetOptions(Resource):
    def get(self):
        '''Retrieves all submitted options from the txt file'''
        if os.path.exists(data_file):
            with open(data_file, 'r') as file:
                options = file.readlines()
            options = [option.strip() for option in options]
        else:
            options = []
        return jsonify({'status': 'success', 'options': options})
