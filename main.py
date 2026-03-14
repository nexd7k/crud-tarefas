from fastapi import FastAPI
import uvicorn
from appdb.tarefasdb import *
from pydantic import BaseModel

app = FastAPI() #Iniciando app
tabela_tarefa() #Iniciando banco

#Criando um modelo base para fazer requisições pelo body no postman
class Tarefa(BaseModel):
    nome: str
    descricao: str

#Home Page
@app.get('/')
async def root():
    return {"CRUD": "Tarefas"}

#CRUD

#Create
@app.post('/tarefas/')
async def criar_tarefas(tarefa: Tarefa):
    #Inserindo um novo dado na tabela (Para inserir, coloque os dados como parametro no Postman)
    cursor.execute('INSERT INTO Tarefas (nome, descricao) VALUES (?, ?)', (tarefa.nome, tarefa.descricao))
    conn.commit()
    return {"message": "Tarefa Cadastrada",
            "id": cursor.lastrowid,
            "nome": tarefa.nome,
            "descrição": tarefa.descricao}

#READ

#Listar todas as tarefas
@app.get('/tarefas')
async def listar_tarefas():
    #Selecionando tudo da tabela
    cursor.execute("SELECT * FROM Tarefas")
    #Salvando todos os dados na variável dados e retornando para mostrar na página
    dados = cursor.fetchall() #cursor.fetchall() para listar todas as tarefas
    if dados is None:
        return {"Erro": "não há nenhuma tarefa."}
    return dados

#Listando apenas uma tarefa baseado no ID
@app.get('/tarefas/{id_tarefa}')
async def listar_uma_tarefa(id_tarefa: int):
    #Selecionando uma tarefa cujo o ID é id_tarefa
    cursor.execute("SELECT * FROM Tarefas WHERE id = ?", (id_tarefa,))
    #Salvando a tarefa na variavel dados e retornando para mostrar na página
    dados = cursor.fetchone()
    if dados is None:
        return {"Erro": "não há nenhuma tarefa."}
    return dados

#UPDATE
@app.put('/tarefas/{id_tarefa}')
async def atualizar_tarefa(tarefa: Tarefa, id_tarefa: int):
    #Selecionando uma tarefa cujo o ID é id_tarefa e preparando para a requisição de atualização
    cursor.execute("UPDATE Tarefas SET nome = ?, descricao = ? WHERE id = ?", (tarefa.nome, tarefa.descricao, id_tarefa,))
    conn.commit()
    return {"Mensagem do sistema": f"Tarefa com ID {id_tarefa} atualizada com sucesso!",
            "Novo nome": f"{tarefa.nome}",
            "Nova descrição": f'{tarefa.descricao}'}

#DELETE
@app.delete('/tarefas/{id_tarefa}')
async def deletar_tarefa(id_tarefa: int):
    #Selecionando e deletando uma tarefa pelo ID
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    return {"message": f"Tarefa de id {id_tarefa} deletada."}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)