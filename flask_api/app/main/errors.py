from flask import jsonify
from app.main import main

@main.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@main.app_errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

