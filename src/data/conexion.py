from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_name = "empleados.sqlite"
engine = create_engine(f"sqlite:///{database_name}")

Session = sessionmaker(bind=engine)
session = Session()

ModeloBase = declarative_base()