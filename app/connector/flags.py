from flask import request
import json
import datetime

class Flags:
    def __init__(self):
        self.flags = []

    def create_a_flag(self):
        new_flag = {
             "id":len(self.flags) + 1,
            "status":"draft",
            "createdBy":"user",
            "createdOn":datetime.datetime.now(),
            "type":request.json['type'],
            "location":request.json['location'],
            "comment":request.json['comment']
        }
        if not all([
            request.json['Type'],
            request.json['location'],
            request.json['comment']
        ]):
            return 'some fields are missing values'
        elif request.json['type'].split() == '':
            return 'Type of flag can not be empty'
        else:
            self.flags.append(new_flag)

    def get_all_redflags(self):
            return flag

    def get_specific_flag(self, id):
        for flag in self.flags:
            if flag['id'] == id:
                return flag
            return 'Flag with this ID is not found'
    
            
    def edit_specific_flag(self, id):
        flag = [flag for flag in self.flags if flag['id']==id]
        if flag:
            flag[0]['status'] = request.json['status']
            flag[0]['createdOn'] = datetime.datetime.now()
            flag[0]['type'] = request.json['type']
            flag[0]['comment'] = request.json['comment']
        else:
            return 'Flag with this ID was not found'

        if not all([
            request.json['status'],
            request.json['type'],
            request.json['comment']
        ]):
             return 'Some fields are missing values'
        elif request.json['status'].strip() == "":
            return 'Flag status can not be empty'
        else:
            return flag

    def delete_specific_flag(self, id):
        for flag in slef.flags:
            if flag['id'] == id:
                self.flags.remove(flag)
                return 'Flag successfully deleted'
            return 'Flag with this ID is not found'
    

