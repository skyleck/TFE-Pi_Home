from flask import jsonify
from flask import request
from flask_restful import Resource
from flask import Flask
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt import current_identity

import sys
sys.path.append("pi_home_core")

from src.be.infokea.pi_home.componentImpl.user.UserImpl import UserImpl
from src.be.infokea.pi_home.utils.UseDB import UseDB
from src.be.infokea.pi_home.domain.User import User

class UserResource(Resource):

    def __init__(self):
        self.userImpl = UserImpl()

    @jwt_required
    def get(self,id=None):
        curent_user = self.userImpl.select(get_jwt_identity())
        if id is None:
            if(curent_user[0].getAuthorization() == 2):
                users = self.userImpl.selectAll()
                return jsonify([e.jsonFormat() for e in users])
            else:
                response = jsonify({'msg': 'Not authorize'})
                response.status_code = 400
                return response
        else:
            print(curent_user[0].getId())
            print(id)
            if curent_user[0].getAuthorization() == 2 or curent_user[0].getId() == int(id):
                users = self.userImpl.select(id)
                return jsonify([e.jsonFormat() for e in users])
            else:
                response = jsonify({'msg': 'Not authorize'})
                response.status_code = 400
                return response

    def post(self):
        content = request.get_json()
        inputVoid = []
        if content["login"] == "":
            inputVoid.append("login")
        if content["firstname"] == "":
            inputVoid.append("firstname")
        if content["lastname"] == "":
            inputVoid.append("lastname")
        if content["password"] == "":
            inputVoid.append("password")
        if content["confirmPassword"] == "":
            inputVoid.append("confirmPassword")
        if len(inputVoid) != 0:
            response = jsonify({'msg': 'One or more fields are not completed', 'column': inputVoid})
            response.status_code = 400
            return response
        if content["password"] != content["confirmPassword"]:
            inputVoid.append("password")
            inputVoid.append("confirmPassword")
            response = jsonify({'msg': 'Passwords not equals', 'column': inputVoid})
            response.status_code = 400
            return response
        checkLogin = self.userImpl.getUserByLogin(content["login"])
        if checkLogin is not None:
            inputVoid.append("login")
            response = jsonify({'msg': 'Login already exist !', 'column': inputVoid})
            response.status_code = 400
            return response
        user = User(0,content["login"],content["firstname"],content["lastname"],content["password"],content["authorization"])
        self.userImpl.insert(user)
        return "User added"

    @jwt_required
    def put(self):
        curent_user = self.userImpl.select(get_jwt_identity())
        content = request.get_json()
        if curent_user[0].getAuthorization() == 2 or curent_user[0].getId() == int(content["id"]):
            inputVoid = []
            if content["login"] == "":
                inputVoid.append("login")
            if content["firstname"] == "":
                inputVoid.append("firstname")
            if content["lastname"] == "":
                inputVoid.append("lastname")
            if content["password"] == "":
                inputVoid.append("password")
            if content["confirmPassword"] == "":
                inputVoid.append("confirmPassword")
            if len(inputVoid) != 0:
                response = jsonify({'msg': 'One or more fields are not completed', 'column': inputVoid})
                response.status_code = 400
                return response
            if content["password"] != content["confirmPassword"]:
                inputVoid.append("password")
                inputVoid.append("confirmPassword")
                response = jsonify({'msg': 'Passwords not equals', 'column': inputVoid})
                response.status_code = 400
                return response
                user = User(content["id"],content["login"],content["firstname"],content["lastname"],content["password"],content["authorization"])
                self.userImpl.updateUser(content["id"],user)
                return "User updated"
        else:
            response = jsonify({'msg': 'Not authorize'})
            response.status_code = 400
            return response

    @jwt_required
    def delete(self,id):
        curent_user = self.userImpl.select(get_jwt_identity())
        if curent_user[0].getAuthorization() == 2 or curent_user[0].getId() == int(id):
            content = request.get_json()
            self.userImpl.delete(id)
            return "User deleted"
        else:
            response = jsonify({'msg': 'Not authorize'})
            response.status_code = 400
            return response