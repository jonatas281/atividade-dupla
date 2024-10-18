import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
BANCO_BANCO = create_engine("sqlite:///bancobanco.db")

# Criando conexão com banco de dados
Session = sessionmaker(bind=BANCO_BANCO)
session = Session()

# Criando tabela
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionarios'

    # Definindo campos da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String)  # Alterado para String
    setor = Column(String)
    funcao = Column(String)
    salario = Column(Integer)
    telefone = Column(String)  # Alterado para String

def adicionar_funcionario(session):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF: ")  # Alterado para String
    setor = input("Digite seu setor: ")
    funcao = input("Digite sua função: ")
    salario = int(input("Digite seu salário: "))
    telefone = input("Digite seu telefone: ")  # Alterado para String

    funcionario_adicionado = Funcionario(
        nome=nome,
        idade=idade,
        cpf=cpf,
        setor=setor,
        funcao=funcao,
        salario=salario,
        telefone=telefone
    )
    session.add(funcionario_adicionado)
    session.commit()
    print("Funcionário adicionado com sucesso!")

def consultar_funcionario(session):
    id_funcionario = int(input("ID do funcionário: "))
    funcionario = session.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
    if funcionario:
        print(f"Funcionário: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}")
    else:
        print("Funcionário não encontrado.")

def atualizar_funcionario(session):
    id_funcionario = int(input("ID do funcionário: "))
    funcionario = session.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
    if funcionario:
        funcionario.nome = input("Novo Nome: ")
        funcionario.idade = int(input("Nova Idade: "))
        funcionario.cpf = input("Novo CPF: ")  # Corrigido
        funcionario.setor = input("Novo Setor: ")
        funcionario.funcao = input("Nova Função: ")
        funcionario.salario = int(input("Novo Salário: "))  # Corrigido
        funcionario.telefone = input("Novo Telefone: ")  # Corrigido
        session.commit()
        print("Funcionário atualizado com sucesso!")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario(session):
    id_funcionario = int(input("ID do funcionário a ser excluído: "))
    funcionario = session.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print(f"{funcionario.nome} excluído com sucesso!")
    else:
        print("Funcionário não encontrado.")

def listar_funcionario(session):
    funcionarios = session.query(Funcionario).all()
    for funcionario in funcionarios:
        print(f"id: {funcionario.id}, nome: {funcionario.nome}, setor: {funcionario.setor}")

# Solicitando dados
while True:
    print("""    \nRH System
           | 1 | - Adicionar funcionário
           | 2 | - Consultar funcionário
           | 3 | - Atualizar dados de funcionário
           | 4 | - Excluir funcionário
           | 5 | - Listar todos os funcionários
           | 0 | - Sair do sistema
          """)
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            adicionar_funcionario(session)
        case 2:
            consultar_funcionario(session)
        case 3:
            atualizar_funcionario(session)
        case 4:
            excluir_funcionario(session)
        case 5:
            listar_funcionario(session)
        case 0:
            print("Saindo do sistema.")
            break
        case _:
            print("Opção inválida.")





