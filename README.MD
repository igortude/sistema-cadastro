# Sistema de Cadastro com Banco de Dados SQLite  
**Feito 100% do zero no 1º semestre de Ciência de Dados**

![Python](https://img.shields.io/badge/python-3.13%2B-blue)  
![SQLite](https://img.shields.io/badge/SQLite-3.46%2B-lightgrey)

## Autor  
**Igor Tude**  
Estudante de Ciência de Dados — 1º semestre  
Fevereiro de 2025

## Sobre o projeto  
Esse é o meu primeiro sistema completo com persistência de dados em banco de dados real.

Tudo foi construído com as próprias mãos, sem copiar código pronto — só com explicações, tentativa, erro e correção.  
O objetivo foi aprender de verdade, não só fazer funcionar.

## Funcionalidades atuais (CRUD em andamento)

- [x] Cadastro de usuários com validação de idade  
- [x] Salvamento automático no banco SQLite (`portfolio2.db`)  
- [x] Exclusão de usuário por ID com verificação (`rowcount`)  
- [x] Listagem de usuários
- [x] Trativa de Erros try,except  
- [ ] Edição de cadastro  
- [ ] Relatórios com pandas + gráficos  
- [ ] Dashboard com Streamlit (próximos passos)

## Estrutura do projeto

cadastro_simples/
├── main.py → programa principal com menu e inputs
├── funcoes.py → funções de banco (inserir, deletar, listar)
├── portfolio2.db → banco de dados SQLite (gerado automaticamente)
├── run_queries.sql → suas queries de análise 
└── README.md → este arquivo

## Como executar
1. Clone o repositório
2. Execute `python main.py` 