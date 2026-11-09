import sqlite3

NOME_BANCO = "cadastro.db"

def criar_banco():
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cursor = db.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS pessoas (
                    cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    altura REAL NOT NULL
                );
                """
            )
            return True
    except sqlite3.Error as erro:
        print(f"Falha na criação do banco: {erro}")
        return False


def cadastrar_pessoa() -> bool:
    pass


def listar_pessoas() -> list:
    pass


def atualizar_pessoa() -> bool:
    pass


def excluir_pessoa() -> bool:
    pass


def buscar_pessoa_por_nome() -> bool:
    pass
