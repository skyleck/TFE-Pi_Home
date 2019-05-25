#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import request
import sys
sys.path.append("pi_home_core")

from src.be.infokea.pi_home.componentImpl.user.UserImpl import UserImpl
from src.be.infokea.pi_home.utils.UseDB import UseDB
from src.be.infokea.pi_home.domain.User import User
from flask_cors import CORS, cross_origin

userImpl = UserImpl(UseDB("192.168.1.155","root","test","pi_home"))

app = Flask(__name__)
cors = CORS(app, support_credentials=True,resources={r"/api/*": {"origins": "*"}})

@app.route('/api/getAllUsers')
def getAllUsers():
    users = userImpl.selectAll()
    return jsonify([e.jsonFormat() for e in users])

@app.route('/api/getUser')
def getUser():
    return "ok"
    
@app.route('/api/login', methods = ['POST'])
def login():
    content = request.get_json()
    print(content)
    user = userImpl.login(content["login"],content["password"])
    print(user)
    if(user == None):
        response = jsonify('Login or password incorrect')
        response.status_code = 400
        return response
    return jsonify([e.jsonFormat() for e in user])

@app.route('/addUser', methods = ['POST'])
def createUser():
    content = request.get_json()
    print (content["firstname"])
    userImpl.insert(User(content["login"],content["firstname"],content["lastname"],content["password"]))
    return "ok"

@app.route('/', methods = ['POST'])
def test():
    print(request.headers)
    print(request.data)
    print(request.form.to_dict())
    print(request.files)
    return "ok"

@app.route("/updateUser", methods = ['PUT'])
def updateUser():
    content = request.get_json()
    user = User(content["login"],content["firstname"],content["lastname"],content["password"])
    print(userImpl.updateUser(content["id"], user))
    return "User updated"

@app.route("/deleteUser", methods = ['DELETE'])
def deleteUser():
    content = request.get_json()
    userImpl.delete(content["id"])
    return "User delete"

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5001)
