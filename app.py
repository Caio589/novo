from flask import Flask, request, jsonify, render_template
from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def painel():
    return render_template("index.html")

# ======================
# RECEBER PEDIDO (CARDÁPIO)
# ======================
@app.route("/novo_pedido", methods=["POST"])
def novo_pedido():
    conn = get_db_connection()
    cur = conn.cursor()

    dados = request.get_json()

    cur.execute("""
        INSERT INTO pedidos (itens, total, observacao)
        VALUES (%s,%s,%s)
    """, (
        dados["itens"],
        dados["total"],
        dados.get("observacao", "")
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Pedido recebido com sucesso"})

# ======================
# LISTAR PEDIDOS (PAINEL)
# ======================
@app.route("/pedidos")
def pedidos():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, itens, total, observacao, status, data
        FROM pedidos
        ORDER BY id DESC
    """)

    lista = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(lista)

# ======================
# ATUALIZAR STATUS
# ======================
@app.route("/status_pedido", methods=["POST"])
def status_pedido():
    conn = get_db_connection()
    cur = conn.cursor()

    dados = request.get_json()

    cur.execute(
        "UPDATE pedidos SET status=%s WHERE id=%s",
        (dados["status"], dados["id"])
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Status atualizado"})


if __name__ == "__main__":
    app.run(debug=True)
