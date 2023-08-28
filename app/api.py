from app import app
from app.models import User, Post
from flask import jsonify


@app.route('/api/users', methods=['GET'])
def get_users():
    data = User.to_collection()
    return jsonify(data)
