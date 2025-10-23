# app.py
from flask import Flask, request, jsonify
from funciones import sumar

app = Flask(__name__)

@app.route('/sumar', methods=['GET'])
def sumar_endpoint():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({'resultado': sumar(a, b)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3069)
