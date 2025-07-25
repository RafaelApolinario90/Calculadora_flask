from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = ''
    if request.method == 'POST':
        expressao = request.form.get('expressao')
        try:
            # Substituições manuais para símbolos que o Python não reconhece
            expressao = expressao.replace('√', 'math.sqrt')
            expressao = expressao.replace('%', '/100')

            resultado = eval(expressao)
        except:
            resultado = 'Erro'
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
