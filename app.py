"""BANCO DE DADOS
    - SQL (LINGUAGEM DE CONSULTA ESTRUTURADA)
    - EXEMPLO:
        - SELECT * FROM CLIENTES;
        - IRÁ CONSULTAR O BD NA TABELA CLIENTES.

        - SGBD:
            - GERENCIAR PERMISSÕES DE ACESSO
            - ADMINISTRADOR DE BANCO DE DADOS (DBA)
            - CRIAR CONSULTAS PERSONALIZADAS

        - ORM: MAPEAMENTO OBJETO RELACIONAL
            - USAR A LINGUAGEM DE PROGRAMAÇÃO 
            PARA MANIPULAR O BANCO DE DADOS.
        - INSTALANDO ORM PARA PYTHON:
            - pip install sqlalchemy
"""

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criandp banco de dados:
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados:
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela:
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    # Definindo campos da tabela:
    ra = Column("ra", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe:
    def __init__(self, ra: int, nome: str, email: str, senha: str):
        self.ra = ra
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando a tabela no banco de dados:
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD:
# C - Create - INSERT - Salvar.
class Salvar():
    os.system("cls || clear")
    print("\nSolicitando dados para o usuário.")
    inserir_ra = input("Digite o seu R.A: ")
    inserir_nome = input("Digite o seu nome: ")
    inserir_email = input("Digite o seu e-mail: ")
    inserir_senha = input("Digite o seu senha: ")

    aluno = Aluno(ra=inserir_ra, nome=inserir_nome, email=inserir_email, senha=inserir_senha)
    session.add(aluno)
    session.commit()

# R - Read - SELECT - Consulta
class Consulta():
    print("\nExibindo dados de todos os usuários na tabela.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.email} - {aluno.senha}")

# U - Update - UPDATE - Atualizar 
class Atualizar():
    print("\nAtualizando dados do usuário.")
    email_aluno = input("Digite o email do aluno que será atualizado: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        aluno.ra = input("Digite o seu R.A: ")
        aluno.nome = input("Digite o seu nome: ")
        aluno.email = input("Digite o seu email: ")
        aluno.senha = input("Digite o seu senha: ")

        session.commit()
    else:
        print("Aluno não encontrado.")

# D - Delete - DELETE - Excluir
class Deletar():
    print("\nExcluindo os dados de um aluno.")
    email_aluno = input("Digite o email do aluno que será excluído: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} excluido com sucesso!")

    else:
        print("Aluno não encontrado.")

# R - Read - SELECT - Consulta
class ConsultarUm():
    print("\nConsultando os dados de apenas um aluno.")
    email_aluno = input("Digite o email do aluno: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.email} - {aluno.senha}")
    else:
        print("Aluno não encontrado.")

#Fechando conexão:
session.close()