### 🔹 3. API DE CADASTRO

```markdown
# 🔐 API de Cadastro de Clientes

API REST desenvolvida com Flask para gerenciamento de clientes, com operações completas de CRUD e persistência em banco de dados SQLite.

## 🚀 Funcionalidades
- Cadastro de clientes
- Listagem de clientes
- Atualização de dados
- Exclusão de registros

## 🧰 Tecnologias
- Python 3
- Flask
- SQLite

## 📡 Rotas

| Método | Endpoint        | Descrição              |
|--------|---------------|----------------------|
| GET    | /clientes     | Lista todos os clientes |
| GET    | /clientes/<id> | Busca cliente por ID |
| POST   | /clientes     | Cria novo cliente |
| PUT    | /clientes/<id> | Atualiza cliente |
| DELETE | /clientes/<id> | Remove cliente |

## ⚙️ Como executar

```bash
git clone https://github.com/NaitySantos/api-cadastro
cd api-cadastro
pip install flask
python app.py
