import sys

from flask import Flask, request

sys.path.append("../")
from controllers.operation_controller import add_to_db, get_filter, get_all
from config import HOST, HTTP_PORT

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask app is working!"


@app.route('/<operator>', methods=['POST', 'GET'])
def calculate(operator):
    n1 = request.args['n1']
    n2 = request.args['n2']
    res = add_to_db(operator, n1, n2)
    return res


@app.route('/filter/<oper>', methods=['POST', 'GET'])
def get_operations(oper):
    if oper:
        res = get_filter(request.args, oper)
    else:
        res = get_all()
    return res


@app.route('/filter/', methods=['POST', 'GET'])
def get_all_operatoins():
    res = get_all()
    return res


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=HTTP_PORT)
