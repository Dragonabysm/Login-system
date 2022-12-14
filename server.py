from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///SistemaLoginCadastro/cadastros.db')
Base = declarative_base(engine)
Session = sessionmaker(engine)
session = Session()


class Registration(Base):
    __tablename__ = 'cadastros'
    id = Column(Integer, primary_key=True)
    email = Column(Text)
    password = Column(Text)


def addRegistration(registration: Registration):
    global session, Base
    Base.metadata.create_all(engine)
    session.add(registration)
    session.commit()


def verifyUser(email: str, password_hash: str):
    global session, Registration
    if session.query(Registration).filter(Registration.email == email, Registration.password == password_hash).all():
        return True
    return False
