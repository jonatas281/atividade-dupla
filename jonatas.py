import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# criando banco de dados
BANCO_BANCO = create_engine("sqlite:///bancobanco.db")

# criando conexão com banco de dados
Session = sessionmaker(bind=BANCO_BANCO)
session = Session()

# criando tabela
Base = declarative_base()

class funcionario(base):
    __tablename__= 'funcionarios'

 # definindo campus da tabela
id = Column("id",Integer, primary_key=True)
nome = Column("nome",String)
idade = Column("idade",Integer) 
cpf = Column("cpf",Integer)
setor = Column("setor",String)
funcao = Column("função",String)
salario = Column("salario",Integer)
telefone = Column("telefone",Integer)

def adicionar_funcionario(session):
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    cpf = int(input("digite seu cpf: "))
    setor = input("digite saeu setor: ")
    funcao = input("digite sua função: ")
    salario = int(input("digite seu salario: "))
    telefone = int(input("digite seu telefone: "))

    funcionario_adicionado= funcionario(funcionario=nome,funcionario=idade,funcionario=cpf
                                        ,funcionario=setor,funcionario=funcao,funcionario=salario,funcionario=telefone)
    session.add(funcionario_adicionado)
    session.commit()
    print("funcionario adicionado com sucesso: ")
def listar_funcionario(session):


