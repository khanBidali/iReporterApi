from app.connector.user import User
from app.connector.flags import Flags
from flask import Flask, jsonify
from app import app

user = User()
flag = Flags()

@app.route('/')
def index():
    return jsonify({'message': 'Welcome To iReporter APP'})

@app.route('/api/v1/login/<string:username>')
def login(username):
    user.login(username)
    return jsonify({'Message':'Logged in successfully'}), 200

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    return jsonify({'Message':user.signup()}), 201


@app.route('/api/v1/users')
def all_users():
    return jsonify({'Users':user.get_all_users()}), 200

@app.route('/api/v1/flags', methods=['POST'])
def create_a_flag():
    return jsonify({'Message':flag.create_a_flag()}), 201

@app.route('/api/v1/flags')
def get_all_flags():
    return jsonify({'Flags':flag.get_all_flags()}), 200

@app.route('/api/v1/flags/<int:id>', methods=['DELETE'])
def delete_one_flag(id):
    return jsonify({'Message':flag.delete_specific_flag(id)}), 200

@app.route('/api/v1/flags<int:id>')
def get_one_flag(id):
    return jsonify({'Flag':flag.get_one_flag()})

@app.route('/api/v1/flags/<int:id>', methods=['PUT'])
def edit_one_flag(id):  
    return jsonify({'Message':flag.edit_specific_flag(id)}), 200
