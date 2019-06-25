import hashlib

from flask import jsonify
from flask import request
from flask_restful import Resource
from flask import Flask
from flask_jwt_extended import create_access_token, create_refresh_token

import sys
sys.path.append("pi_home_core")

from src.be.infokea.pi_home.componentImpl.user.UserImpl import UserImpl
from src.be.infokea.pi_home.utils.UseDB import UseDB
from src.be.infokea.pi_home.domain.User import User

class LoginRessource(Resource):

    def post(self):
        content = request.get_json()
        userImpl = UserImpl()
        user = userImpl.login(content["login"],content["password"])
        print(user)
        if(user == None):
            response = jsonify('Login or password incorrect')
            response.status_code = 400
            return response
        access_token = create_access_token(identity = str(user[0].getId()))
        refresh_token = create_refresh_token(identity = str(user[0].getId()))
        return{
            'message': 'Logged in as ' + str(user[0].getLogin()),
            'access_token':access_token,
            'refresh_token':refresh_token,
            'id': str(user[0].getId())
        }