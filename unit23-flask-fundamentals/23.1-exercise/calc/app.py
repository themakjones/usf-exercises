from flask import Flask, request

app = Flask(__name__)

import operations

@app.route('/add', methods=['GET'])
def add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{operations.add(a,b)}'

@app.route('/sub', methods=['GET'])
def sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{operations.sub(a,b)}'

@app.route('/mult', methods=['GET'])
def mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{operations.mult(a,b)}'

@app.route('/div', methods=['GET'])
def div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{operations.div(a,b)}'

math_oper = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

@app.route('/math/<operation>')
def math_add(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{math_oper[operation](a,b)}'