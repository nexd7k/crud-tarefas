API de Tarefas com FastAPI

Este projeto é uma API simples de gerenciamento de tarefas desenvolvida em Python utilizando FastAPI e SQLite. A aplicação permite criar, listar, atualizar e deletar tarefas através de requisições HTTP.

Tecnologias utilizadas

Python
FastAPI
SQLite
Uvicorn
Pydantic

Funcionalidades

Criar tarefas
Listar todas as tarefas
Buscar uma tarefa pelo ID
Atualizar uma tarefa
Deletar uma tarefa


Endpoints da API

GET /
Retorna a página inicial.

POST /tarefas/
Cria uma nova tarefa.

GET /tarefas
Lista todas as tarefas.

GET /tarefas/{id_tarefa}
Retorna uma tarefa específica pelo ID.

PUT /tarefas/{id_tarefa}
Atualiza uma tarefa existente.

DELETE /tarefas/{id_tarefa}
Remove uma tarefa pelo ID.
