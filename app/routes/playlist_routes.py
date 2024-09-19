from flask import request, jsonify
from . import playlist_bp

playlists = []

@playlist_bp.route('/playlists', methods=['GET'])
def get_playlists():
    return jsonify(playlists)

@playlist_bp.route('/playlists', methods=['POST'])
def add_playlist():
    new_playlist = request.json.get('playlist')
    if not new_playlist:
        return jsonify({"error": "No playlist provided"}), 400

    playlists.append(new_playlist)
    return jsonify({"message": "Playlist added"}), 201
