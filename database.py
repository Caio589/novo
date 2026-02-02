import psycopg2
import os

_inicializado = False

def get_db_connection():
    global _inicializado

    conn = psycopg2.connect(
        os.environ["DATABASE_URL"],
        sslmode="require"
    )

    if not _inicializado:
        criar_estrutura(conn)
        _inicializado = True

    return conn


def criar_estrutura(conn):
    cur = conn.cursor()

    # PEDIDOS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            itens TEXT,
            total NUMERIC(10,2),
            observacao TEXT,
            status VARCHAR(20) DEFAULT 'novo',
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cur.close()
