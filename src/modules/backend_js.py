import sys
from .shipment import Shipment

class Capture():
    def __init__(self,*args, **kwargs):
        self.embarque = Shipment()

        print("")
#captura de datos de embarque
# embarque ,operacion ,unidad ,origen ,destiono ,referencia , cliente

    def Capture_shipment(self, shipment):
        #result = "{}".format(shipment)
        result = shipment.keys()
        
        print(result)
        
        #self.embarque.client_reference = shipment.get("embarque")
        #self.embarque.type_operation = shipment.get("operacion")
        #self.embarque.unit_truck = shipment.get("unidad")
        #self.embarque.pickup= shipment.get("origen")
        #self.embarque.deliverto = shipment.get("destino")
        #self.embarque.internal_reference = shipment.get("referencia")
        #self.embarque.client = shipment.get("cliente")
        
        #print(self.embarque.client_reference, self.embarque.type_operation ,self.embarque.unit_truck, self.embarque.pickup, self.embarque.deliverto, self.embarque.internal_reference, self.embarque.client)
    def getdata(self):
        precapture=  self.embarque.send_precapture
        
        print(precapture)
        return precapture