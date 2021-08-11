from chalice import Chalice
import boto3
from chalicelib.utils import hello

app = Chalice(app_name='simple-example')
app.debug = True


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route("/test")
def test():
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name='remelo', WithDecryption=True)
    return parameter['Parameter']['Value']


@app.route('/vivanuncios', methods=['POST'])
def create_user(event, context):
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return user_as_json


@app.route('/hello', methods=['POST'])
def hello_test():
    return hello()

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
