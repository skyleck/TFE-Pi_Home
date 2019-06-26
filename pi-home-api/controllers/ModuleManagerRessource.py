from flask import jsonify
from flask import request
from flask_restful import Resource
from flask import Flask
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt import current_identity

import sys
sys.path.append("pi_home_core")

from src.be.infokea.pi_home.componentImpl.module.ModuleImpl import ModuleImpl
from src.be.infokea.pi_home.domain.Module import Module

from src.be.infokea.pi_home.componentImpl.user.UserImpl import UserImpl
from src.be.infokea.pi_home.domain.User import User

class ModuleManagerRessource(Resource):

    def __init__(self):
        self.moduleImpl = ModuleImpl()
        self.userImpl = UserImpl()

    @jwt_required
    def get(self,id=None):
        curent_user = self.userImpl.select(get_jwt_identity())
        if id is None:
            if(curent_user[0].getAuthorization() == 2):
                modules = self.moduleImpl.selectAll()
                return jsonify([e.jsonFormat() for e in modules])
            else:
                response = jsonify({'msg': 'Not authorize'})
                response.status_code = 400
                return response
        else:
            if curent_user[0].getAuthorization() == 2 or curent_user[0].getId() == int(id):
                users = self.moduleImpl.select(id)
                return jsonify([e.jsonFormat() for e in users])
            else:
                response = jsonify({'msg': 'Not authorize'})
                response.status_code = 400
                return response 

    def post(self):
        content = request.get_json()
        module = Module(0,"None",content["ip"],0)
        self.moduleImpl.insert(module)
        return "Module added"

    
