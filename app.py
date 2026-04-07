from flask import Flask, render_template

app = Flask(__name__)

# Rota para a Página Inicial (INÍCIO)
@app.route('/')
def inicio():
    return render_template('inicio.html')

# Rota para a Página de Serviços (SERVIÇOS)
@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

# Rota para a Página de Contacto (CONTACTO)
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    # debug=True para te ajudar no desenvolvimento,
    # mas não deve ser usado no site final publicado.
    app.run(debug=True)