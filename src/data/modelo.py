from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, CHAR, TEXT, ForeignKey, create_engine

ModeloBase = declarative_base()

class Employee(ModeloBase):
    __tablename__ = 'employee'

    id_employee = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(55), nullable=False)
    lastname = Column(String(55), nullable=False)
    garden = Column(CHAR(1), nullable=False)
    cellphone = Column(String(50))
    charge = Column(String(50), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(150), nullable=False)
    state = Column(String(150), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    birthday = Column(String(12), nullable=False)
    create_stamp = Column(TEXT, default=func.strftime('%Y-%m-%d %H:%M:%S', 'now()'))

    usernames = relationship("Username", back_populates="employee")
    unittrucks = relationship("Unittruck", back_populates="employee")
    trailers = relationship("Trailer", back_populates="employee")
    assigned_shipments = relationship("AssginShipment", back_populates="driver_employee")

class Username(ModeloBase):
    __tablename__ = 'username'

    id_username = Column(Integer, primary_key=True, autoincrement=True)
    id_employee = Column(Integer, ForeignKey('employee.id_employee'))
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    admit = Column(CHAR(1), nullable=False)

    employee = relationship("Employee", back_populates="usernames")
    assigned_shipments = relationship("AssginShipment", back_populates="assigned_by_user")

class Unittruck(ModeloBase):
    __tablename__ = 'unittruck'

    id_driver = Column(Integer, primary_key=True, autoincrement=True)
    driver = Column(Integer, ForeignKey('employee.id_employee'))
    trucknumber = Column(String(100), unique=True, nullable=False)
    truckplates = Column(String(50), unique=True, nullable=False)
    working = Column(String(25), nullable=False, default='yes')

    employee = relationship("Employee", back_populates="unittrucks")
    trailers = relationship("Trailer", back_populates="unittruck")
    assigned_shipments = relationship("AssginShipment", back_populates="unit_truck")

class Trailer(ModeloBase):
    __tablename__ = 'trailer'

    id_truck = Column(Integer, primary_key=True, autoincrement=True)
    driver = Column(Integer, ForeignKey('employee.id_employee'))
    unittruck = Column(Integer, ForeignKey('unittruck.id_driver'))
    trailer = Column(String(250), nullable=False)
    trailer_plate = Column(String(50), nullable=False)
    seal = Column(String(100), nullable=False)
    trailer_type = Column(String(50), nullable=False, default='53ft')
    conditions = Column(String(255), nullable=False, default='en condiciones')
    registrate = Column(TEXT, default=func.strftime('%Y-%m-%d %H:%M:%S', 'now()'))

    employee = relationship("Employee", back_populates="trailers")
    unittruck = relationship("Unittruck", back_populates="trailers")
    assigned_shipments = relationship("AssginShipment", back_populates="trailer")

class Costumer(ModeloBase):
    __tablename__ = 'costumer'

    id_company = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    assigned_shipments = relationship("AssginShipment", back_populates="costumer")

class Origen(ModeloBase):
    __tablename__ = 'origen'

    id_origen = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    address = Column(String(255))
    registrate = Column(TEXT, nullable=False, default=func.strftime('%Y-%m-%d %H:%M:%S', 'now()'))

    assigned_shipments_pickup = relationship("AssginShipment", foreign_keys='[AssginShipment.pickup]', back_populates="pickup_location")
    arrivals = relationship("Arrival", back_populates="origen")
    complete_trips = relationship("CompleteTrip", back_populates="arrival_location")

class Destination(ModeloBase):
    __tablename__ = 'destination'

    id_destination = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255))
    registrate = Column(TEXT, default=func.strftime('%Y-%m-%d %H:%M:%S', 'now()'))

    assigned_shipments_deliver = relationship("AssginShipment", foreign_keys='[AssginShipment.deliver]', back_populates="deliver_location")
    deliveries = relationship("Deliver", back_populates="destination")

class AssginShipment(ModeloBase):
    __tablename__ = 'assgin_shipment'

    id_shipment = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(String(255), nullable=False, unique=True)
    ref_company = Column(String(255), nullable=False, default='N/A')
    driver = Column(Integer, ForeignKey('employee.id_employee'))
    id_uniittruck = Column(Integer, ForeignKey('unittruck.id_driver'))
    id_trailer = Column(Integer, ForeignKey('trailer.id_truck'), nullable=True)
    id_client = Column(Integer, ForeignKey('costumer.id_company'))
    assignedby = Column(Integer, ForeignKey('username.id_username'))
    pickup = Column(Integer, ForeignKey('origen.id_origen'))
    deliver = Column(Integer, ForeignKey('destination.id_destination'))

    driver_employee = relationship("Employee", back_populates="assigned_shipments")
    unit_truck = relationship("Unittruck", back_populates="assigned_shipments")
    trailer = relationship("Trailer", back_populates="assigned_shipments")
    costumer = relationship("Costumer", back_populates="assigned_shipments")
    assigned_by_user = relationship("Username", back_populates="assigned_shipments")
    pickup_location = relationship("Origen", foreign_keys=[pickup], back_populates="assigned_shipments_pickup")
    deliver_location = relationship("Destination", foreign_keys=[deliver], back_populates="assigned_shipments_deliver")
    arrivals = relationship("Arrival", back_populates="assgin_shipment")
    pickups = relationship("Pickup", back_populates="assgin_shipment")
    inspections_mx = relationship("InspectionMX", back_populates="assgin_shipment")
    clear_mxes = relationship("ClearMx", back_populates="assgin_shipment")
    clear_usas = relationship("ClearUsa", back_populates="assgin_shipment")
    inspections_usa = relationship("InspectionUsa", back_populates="assgin_shipment")
    safe_yards = relationship("SafeYard", back_populates="assgin_shipment")
    deliveries = relationship("Deliver", back_populates="assgin_shipment")

class Arrival(ModeloBase):
    __tablename__ = 'arrival'

    id_arrival = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(String, ForeignKey('assgin_shipment.ref_shipment'))
    date = Column(String(50))
    comments = Column(String(255), default='llegada a origen')
    trailerfail = Column(String(100), default='en condiciones')

    assgin_shipment = relationship("AssginShipment", back_populates="arrivals")
    origen = relationship("Origen", back_populates="arrivals")
    complete_trip = relationship("CompleteTrip", back_populates="arrival")

class Pickup(ModeloBase):
    __tablename__ = 'pickup'

    id_pickup = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(Integer, ForeignKey('assgin_shipment.id_shipment'))
    date = Column(String(50))
    comments = Column(String(255), default='recolectando caja')

    assgin_shipment = relationship("AssginShipment", back_populates="pickups")
    complete_trip = relationship("CompleteTrip", back_populates="pickup")

class InspectionMX(ModeloBase):
    __tablename__ = 'inspection_MX'

    id_inspection_MX = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(Integer, ForeignKey('assgin_shipment.id_shipment'))
    date = Column(String(50))
    new_seal = Column(String(50))
    comments = Column(String(255))

    assgin_shipment = relationship("AssginShipment", back_populates="inspections_mx")
    complete_trip = relationship("CompleteTrip", back_populates="mx_inspection")

class ClearMx(ModeloBase):
    __tablename__ = 'clear_mx'

    id_clear_mx = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(Integer, ForeignKey('assgin_shipment.id_shipment'))
    date = Column(String(50))
    comments = Column(String(255), default='saliendo de aduana MX')

    assgin_shipment = relationship("AssginShipment", back_populates="clear_mxes")
    complete_trip = relationship("CompleteTrip", back_populates="mx_clear")

class ClearUsa(ModeloBase):
    __tablename__ = 'clear_usa'

    id_clear_usa = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(Integer, ForeignKey('assgin_shipment.id_shipment'))
    date = Column(String(50))
    comments = Column(String(255), default='Rojo Mx')

    assgin_shipment = relationship("AssginShipment", back_populates="clear_usas")
    complete_trip = relationship("CompleteTrip", back_populates="usa_clear")

class InspectionUsa(ModeloBase):
    __tablename__ = 'inspection_usa'

    id_inspection_usa = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(Integer, ForeignKey('assgin_shipment.id_shipment'))
    date = Column(String(50))
    new_seal = Column(String(50))
    comments = Column(String(255), default='Rojo Usa')

    assgin_shipment = relationship("AssginShipment", back_populates="inspections_usa")
    complete_trip = relationship("CompleteTrip", back_populates="usa_inspection")

class SafeYard(ModeloBase):
    __tablename__ = 'safe_yard'

    id_safe_yard = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(Integer, ForeignKey('assgin_shipment.id_shipment'))
    date = Column(String(50))
    comments = Column(String(255))

    assgin_shipment = relationship("AssginShipment", back_populates="safe_yards")
    complete_trip = relationship("CompleteTrip", back_populates="usa_safe_yard")

class Deliver(ModeloBase):
    __tablename__ = 'deliver'

    id_deliver = Column(Integer, primary_key=True, autoincrement=True)
    ref_shipment = Column(Integer, ForeignKey('assgin_shipment.id_shipment'))
    date = Column(String(50))
    comments = Column(String(255))

    assgin_shipment = relationship("AssginShipment", back_populates="deliveries")
    destination = relationship("Destination", back_populates="deliveries")
    complete_trip = relationship("CompleteTrip", back_populates="delivered")

class CompleteTrip(ModeloBase):
    __tablename__ = 'complete_trip'

    id_complete = Column(Integer, primary_key=True, autoincrement=True)
    arrival = Column(Integer, ForeignKey('origen.id_origen'))
    pickup = Column(Integer, ForeignKey('pickup.id_pickup'))
    mx_clear = Column(Integer, ForeignKey('clear_mx.id_clear_mx'))
    mx_inspecction = Column(Integer, ForeignKey('inspection_MX.id_inspection_MX'))
    usa_clear = Column(Integer, ForeignKey('clear_usa.id_clear_usa'))
    usa_inspecction = Column(Integer, ForeignKey('inspection_usa.id_inspection_usa'))
    usa_safe_yard = Column(Integer, ForeignKey('safe_yard.id_safe_yard'))
    delivered = Column(Integer, ForeignKey('deliver.id_deliver'))
    done = Column(CHAR(1), nullable=False)

    arrival_location = relationship("Origen", back_populates="complete_trips")
    pickup = relationship("Pickup", back_populates="complete_trip")
    mx_clear = relationship("ClearMx", back_populates="complete_trip")
    mx_inspection = relationship("InspectionMX", back_populates="complete_trip")
    usa_clear = relationship("ClearUsa", back_populates="complete_trip")
    usa_inspection = relationship("InspectionUsa", back_populates="complete_trip")
    usa_safe_yard = relationship("SafeYard", back_populates="complete_trip")
    delivered = relationship("Deliver", back_populates="complete_trip")

# Example of how to create an engine and metadata (not executing DDL)
engine = create_engine('sqlite:///:memory:') # Replace with your database URL
ModeloBase.metadata.create_all(engine)