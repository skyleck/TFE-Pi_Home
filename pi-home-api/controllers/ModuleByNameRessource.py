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

class ModuleByNameRessource(Resource):

    def __init__(self):
        self.moduleImpl = ModuleImpl()
        self.userImpl = UserImpl()

    def get(self, name):
        modules = self.moduleImpl.selectByName(name)
        if(modules is None):
            return []
        return jsonify([e.jsonFormat() for e in modules])
