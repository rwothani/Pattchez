from flask import Blueprint

# Blueprint instances for each set of routes
auth_bp = Blueprint('auth', __name__)
chat_bp = Blueprint('chat', __name__)
journal_bp = Blueprint('journal', __name__)
resource_bp = Blueprint('resource', __name__)
playlist_bp = Blueprint('playlist', __name__)

# Import the routes to register them
from . import auth_routes, chat_routes, journal_routes, resource_routes, playlist_routes
