from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

@app.route('/factorial', methods=['GET'])
def factorial():
    try:
        num = int(request.args.get('numero'))
        resultado = calcular_factorial(num)
        if resultado is None:
            return jsonify({'error': 'Ingresa un número positivo'}), 400
        return jsonify({'numero': num, 'factorial': resultado})
    except ValueError:
        return jsonify({'error': 'Debes ingresar un número válido'}), 400

if __name__ == '__main__':
    app.run(debug=True)
