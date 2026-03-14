import sqlite3

conn = sqlite3.connect("appdb.db")
cursor = conn.cursor()

def tabela_tarefa():
    conn.execute(
        """
        CREATE TABLE IF NOT  EXISTS Tarefas (

        id INTEGER PRIMARY KEY,
        nome CHAR (20),
        descricao CHAR(50)

        )
        """
    )
    conn.commit() #Usar conn.commit() quando for fazer alguma mudança no banco (inserir, atualizar e deletar)