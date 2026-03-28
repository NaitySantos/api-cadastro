from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ============================================================
# Banco de dados — cria a tabela se nao existir
# ============================================================

def init_db():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT
        )
    """)
    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect("clientes.db")
    conn.row_factory = sqlite3.Row
    return conn


# ============================================================
# Rotas da API
# ============================================================

# Listar todos os clientes
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    conn = get_db()
    clientes = conn.execute("SELECT * FROM clientes").fetchall()
    conn.close()
    return jsonify([dict(c) for c in clientes])


# Buscar um cliente por ID
@app.route("/clientes/<int:id>", methods=["GET"])
def buscar_cliente(id):
    conn = get_db()
    cliente = conn.execute("SELECT * FROM clientes WHERE id = ?", (id,)).fetchone()
    conn.close()
    if cliente:
        return jsonify(dict(cliente))
    return jsonify({"erro": "Cliente nao encontrado"}), 404


# Cadastrar novo cliente
@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone", "")

    if not nome or not email:
        return jsonify({"erro": "Nome e email sao obrigatorios"}), 400

    conn = get_db()
    conn.execute(
        "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
        (nome, email, telefone)
    )
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"}), 201


# Atualizar cliente
@app.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    dados = request.get_json()
    conn = get_db()
    cliente = conn.execute("SELECT * FROM clientes WHERE id = ?", (id,)).fetchone()

    if not cliente:
        conn.close()
        return jsonify({"erro": "Cliente nao encontrado"}), 404

    nome = dados.get("nome", cliente["nome"])
    email = dados.get("email", cliente["email"])
    telefone = dados.get("telefone", cliente["telefone"])

    conn.execute(
        "UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?",
        (nome, email, telefone, id)
    )
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Cliente atualizado com sucesso!"})


# Deletar cliente
@app.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    conn = get_db()
    cliente = conn.execute("SELECT * FROM clientes WHERE id = ?", (id,)).fetchone()

    if not cliente:
        conn.close()
        return jsonify({"erro": "Cliente nao encontrado"}), 404

    conn.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Cliente deletado com sucesso!"})


# ============================================================
# Inicia o servidor
# ============================================================

if __name__ == "__main__":
    init_db()
    print("[API] Servidor rodando em http://localhost:5000")
    print("[API] Rotas disponíveis:")
    print("  GET    /clientes        - lista todos")
    print("  GET    /clientes/<id>   - busca um")
    print("  POST   /clientes        - cadastra novo")
    print("  PUT    /clientes/<id>   - atualiza")
    print("  DELETE /clientes/<id>   - deleta")
    app.run(debug=True)