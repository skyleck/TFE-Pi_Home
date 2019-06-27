
from flask import jsonify
from flask import request
from flask_restful import Resource
from flask import Flask
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_jwt import current_identity

import sys
import os
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
                modules = self.moduleImpl.selectNotNone()
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

    def put(self):
        content = request.get_json()
        if("action" in content and content["action"] == "changeState"):
            if(content["state"] == 1):
                value = "On"
            else:
                value = "Off"
            command = "ServerCommandPublish " + value + " " + content["name"]
            os.system(command)
        else:
            if(content["name"] != "None"):
                checkName = self.moduleImpl.selectByName(content["name"])
                if checkName is not None:
                    response = jsonify({'msg': 'Name ' + content["name"] + ' already exist !'})
                    response.status_code = 400
                    return response
                command = "ServerCommandPublishConnected " + content["ip"] + " " + content["name"]
                os.system(command)
            else:
                response = jsonify({'msg': 'None is not a valid name'})
                response.status_code = 400
                return response

        module = Module(content["id"],content["name"],content["ip"],content["state"])
        self.moduleImpl.update(content["id"],module)
        return "Module updated"
        
    def delete(self,id):
        self.moduleImpl.delete(id)
        return "Module deleted"
    
