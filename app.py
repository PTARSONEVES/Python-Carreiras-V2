from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Analista de Dados Senior',
    'localidade': 'PE, Brasil',
    'salario': 'R$ 5.000'
}, {
    'id': 2,
    'titulo': 'Desenvolvedor Front-end',
    'localidade': 'PE, Brasil',
    'salario': 'R$ 5.000'
}, {
    'id': 3,
    'titulo': 'Desenvolvedor Back-end',
    'localidade': 'PE, Brasil',
    'salario': 'R$ 5.000'
}, {
    'id': 4,
    'titulo': 'Desenvolvedor Web',
    'localidade': 'PE, Brasil',
    'salario': 'R$ 5.000'
}, {
    'id': 5,
    'titulo': 'Estatistico',
    'localidade': 'PE, Brasil',
    'salario': 'R$ 5.000'
}]


@app.route("/")
def page_home():
    return render_template('home.html', vagas=VAGAS)


@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGAS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
