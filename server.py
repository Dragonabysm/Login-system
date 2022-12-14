from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///SistemaLoginCadastro/cadastros.db')
Base = declarative_base(engine)
Session = sessionmaker(engine)
session = Session()


class Cadastro(Base):
    __tablename__ = 'cadastros'
    id = Column(Integer, primary_key=True)
    email = Column(Text)
    senha = Column(Text)


def addCadastro(cadastro: Cadastro):
    global session, Base
    Base.metadata.create_all(engine)
    session.add(cadastro)
    session.commit()


def verificarCadastro(email: str, senha_hash: str):
    global session, Cadastro
    if session.query(Cadastro).filter(Cadastro.email==email, Cadastro.senha==senha_hash).all():
        return True
    return False
