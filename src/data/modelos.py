from conexion import ModeloBase
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

class Departamento(ModeloBase):
    __tablename__ = "departamento"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre

    # Add this __repr__ method
    def __repr__(self):
        return f"Departamento : id={self.id}, nombre='{self.nombre}'"

class Empleado(ModeloBase):
    __tablename__ = "empleado"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    documento = Column(String, nullable=False, unique=True)
    id_departamento = Column(Integer, ForeignKey("departamento.id"))

    departamento = relationship("Departamento", backref="empleados") # Added backref for easier access

    def __init__(self, nombre, apellido, documento, id_departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.id_departamento = id_departamento

    # Add this __repr__ method
    def __repr__(self):
        return f"Empleado: \nid={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', documento='{self.documento}', departamento_id={self.id_departamento}"