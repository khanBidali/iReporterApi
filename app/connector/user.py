from flask import request, jsonify
import json
import datetime

class User:
    def __init__(self):
        self.users = []

    def login(self, username):
        user = [user for user in self.users if user['username'] == request.json['username']]
        if user == True:
            return 'Logged in'
        else:
            return jsonify({'Error':'User not found!'})

    def signup(self):
        new_user = {
            "id":len(self.users) + 1,
            "firstname":request.json['firstname'],
            "lastname":request.json['lastname'],
            "email":request.json['email'],
            "phonenumber":request.json['phonenumber'],
            "username":request.json['username'],
            "registered":datetime.datetime.now(),
            "isAdmin":False
        }
        if not all([
            request.json['firstname'],
            request.json['lastname'],
            request.json['email'],
            request.json['phonenumber'],
            request.json['username']
        ]):
            return 'Some fields are missing values'
        elif request.json['firstname'].strip() == "":
            return 'First name can not be empty'
        else:
            self.users.append(new_user)
            return 'User successfully created'

    
    def logout(self):
        exit()
        return jsonify({'message':'Logged out successfully'})
        
    def get_all_users(self):
        return self.users

    def under_investigation(self):
        pass
    def rejected(self):
        pass

    def resolved(self):
        pass