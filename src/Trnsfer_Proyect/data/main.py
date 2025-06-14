from modelos import Departamento, Empleado
from conexion import engine, ModeloBase, session


def guardar_datos():
    contabilidad = Departamento("Contabilidad")
    session.add(contabilidad)
    tecnologia = Departamento("Tecnología")
    session.add(tecnologia)
    session.commit()

    emilio = Empleado("Emilio", "Tafur", "123", contabilidad.id)
    session.add(emilio)
    javier = Empleado("Javier", "Quiñonez", "1234", tecnologia.id)
    session.add(javier)
    session.commit()

    print(contabilidad.id)


def hacer_consultas():
    #para encontrar atravez de su llave primaria
    departamento_1 = session.get(Departamento, 1)
    print(departamento_1)

    #contabilizar los renglones
    cantidad_departamentos = session.query(Departamento).count()
    print(cantidad_departamentos)


    #busqueda con filtro 'where'
    empleados_contabilidad = session.query(Empleado).filter_by(
        id_departamento=departamento_1.id
    ).first()
    print("consulta" , empleados_contabilidad)
    
    allDepartments = session.query(Departamento).all()
    print(allDepartments)


if __name__ == "__main__":
    ModeloBase.metadata.create_all(engine)
    #guardar_datos()
    hacer_consultas()