from flask import Flask, jsonify
from flask_cors import CORS
from desafio import Desafio

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

@app.route("/informacoesNotebooks", methods=["GET"])
def informacoesNoteboooks():
    try:
        desafio = Desafio()
        return jsonify(desafio.encontrarNotebooks()),200
    except Exception as e:
        return "Ocorreu um erro ao executar a rota:"+str(e), 400

if __name__=="__main__":
    app.run()