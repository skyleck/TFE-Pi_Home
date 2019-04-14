from flask import(
    Flask,
    render_template,
    request
)
from flask_cors import CORS
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__, template_folder="templates")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/getUser')
def createUSer():
    return 'createUser'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

