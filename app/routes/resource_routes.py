from flask import request, jsonify
from . import resource_bp

resources = []

@resource_bp.route('/resources', methods=['GET'])
def get_resources():
    return jsonify(resources)

@resource_bp.route('/resources', methods=['POST'])
def add_resource():
    new_resource = request.json.get('resource')
    if not new_resource:
        return jsonify({"error": "No resource provided"}), 400

    resources.append(new_resource)
    return jsonify({"message": "Resource added"}), 201
