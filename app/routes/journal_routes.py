from flask import request, jsonify
from . import journal_bp

# In-memory storage for demonstration purposes
journal_entries = []

@journal_bp.route('/journal', methods=['GET'])
def get_entries():
    # Return all journal entries
    return jsonify(journal_entries)

@journal_bp.route('/journal', methods=['POST'])
def add_entry():
    new_entry = request.json.get('entry')
    if not new_entry:
        return jsonify({"error": "No entry provided"}), 400

    journal_entries.append(new_entry)
    return jsonify({"message": "Entry added"}), 201
