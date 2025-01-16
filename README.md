# DDD-Python API

Este repositório contém uma implementação de um projeto seguindo os princípios de **Domain-Driven Design (DDD)** e **Clean Architecture** em Python. O diretório **API** foca na camada de aplicação, utilizando ferramentas modernas para construir uma API robusta e escalável.

---

## 🚀 Recursos Principais

- **Domain-Driven Design (DDD):** Separação clara de responsabilidades entre domínios.
- **Clean Architecture:** Modularidade e independência de frameworks.
- **Banco de Dados PostgreSQL:** Gerenciamento de dados com `SQLAlchemy` e migrações com `Alembic`.
- **Docker:** Configuração para ambiente de desenvolvimento com Docker Compose.
- **Autenticação Segura:** Criptografia de senhas.
- **Middleware:** Tratamento de requisições e respostas.

---

## 📂 Estrutura do Projeto

Abaixo, uma visão geral da estrutura de pastas:

```
api/
├── .vscode/          # Configurações do editor
├── alembic/          # Migrações de banco de dados
├── src/              # Código fonte da aplicação
│   ├── domain/       # Lógica de negócio
│   ├── application/  # Casos de uso
│   ├── infrastructure/ # Integrações externas (DB, API, etc.)
├── .env.example      # Variáveis de ambiente de exemplo
├── docker-compose.yml # Configuração Docker
├── requirements.txt  # Dependências do projeto
├── run.py            # Ponto de entrada principal
```

---

## 🛠️ Configuração e Execução

### Pré-requisitos

- **Python 3.10+**
- **Docker** e **Docker Compose**

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/lfqcamargo/DDD-Python.git
   cd DDD-Python/api
   ```

2. Crie e configure o arquivo `.env`:
   ```bash
   cp .env.example .env
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute os contêineres Docker:
   ```bash
   docker-compose up
   ```

5. Execute a aplicação localmente:
   ```bash
   python run.py
   ```

---

## ⚙️ Tecnologias Utilizadas

- **FastAPI**: Framework para criação da API.
- **PostgreSQL**: Banco de dados relacional.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **Alembic**: Controle de versões do esquema de banco de dados.
- **Docker/Docker Compose**: Containerização para ambiente de desenvolvimento.

