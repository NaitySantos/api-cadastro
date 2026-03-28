# API de Cadastro de Clientes

API REST em Python com Flask e banco de dados SQLite para cadastro de clientes.

## Tecnologias
- Python 3
- Flask
- SQLite

## Rotas disponíveis
- GET    /clientes        - lista todos os clientes
- GET    /clientes/<id>   - busca um cliente por ID
- POST   /clientes        - cadastra novo cliente
- PUT    /clientes/<id>   - atualiza um cliente
- DELETE /clientes/<id>   - deleta um cliente

## Como usar
1. Clone o repositorio
2. Instale as dependencias: pip install flask
3. Rode: python app.py
4. Acesse http://localhost:5000/clientes

## Exemplo de cadastro
Envie um POST para /clientes com o seguinte JSON:
{
  "nome": "Maria Si
