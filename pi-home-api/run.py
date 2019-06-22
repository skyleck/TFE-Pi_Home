#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import request
from flask_jwt_extended import JWTManager
from flask_restful import Api
import sys
sys.path.append("pi_home_core")

from src.be.infokea.pi_home.componentImpl.user.UserImpl import UserImpl
from src.be.infokea.pi_home.utils.UseDB import UseDB
from src.be.infokea.pi_home.domain.User import User
from flask_cors import CORS, cross_origin

from controllers.LoginRessource import LoginRessource
from controllers.UserResource import UserResource

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
cors = CORS(app, support_credentials=True,resources={r"/api/*": {"origins": "*"}})
api = Api(app)

jwt = JWTManager(app)

api.add_resource(LoginRessource, '/api/login')
api.add_resource(UserResource, "/api/user", "/api/user/<id>")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5001)
