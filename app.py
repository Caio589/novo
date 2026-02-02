from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pedidos = []  # só em memória por enquanto

@app.route("/novo_pedido", methods=["POST"])
def novo_pedido():
    dados = request.get_json()
    pedidos.append(dados)
    return jsonify({"ok": True})

@app.route("/pedidos")
def listar_pedidos():
    return jsonify(pedidos)

if __name__ == "__main__":
    app.run(debug=True)
