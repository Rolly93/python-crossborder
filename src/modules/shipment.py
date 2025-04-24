
class Shipment():
    
    def __init__(self, *args, **kwargs):
        self._client_reference = None #referencia_externa
        self._type_operation = None #impor / exportacion
        self._trailer = None #caja
        self._unit_truck=None #unidad
        self._internal_reference= None #referencia interna
        self._client=None #cliente
        self._pickup = None #donde se recolecta
        self._deliverto = None #donde se entrega
        self._date_time = None
        self._event=None
        self._comments = None
        self._seal=None
        self._safe_yard=None
        
        @property
        def client_reference(self):
            return self._client_reference
        @client_reference.setter
        def client_reference(self,value):
            self._client_reference = value
            
        @client_reference.getter
        def client_reference(self,value):
            self._client_reference = value

        @property
        def type_operation(self):
            return self._client_reference
        @type_operation.setter
        def type_operation(self,value):
            self._client_reference = value


        @property
        def trailer(self):
            return self._client_reference
        @trailer.setter
        def trailer(self,value):
            self._client_reference = value


        @property
        def unit_truck(self):
            return self._client_reference
        @unit_truck.setter
        def unit_truck(self,value):
            self._client_reference = value


        @property
        def internal_reference(self):
            return self._client_reference
        @internal_reference.setter
        def internal_reference(self,value):
            self._client_reference = value
            

        
        @property
        def client(self):
            return self._client_reference
        @client.setter
        def client(self,value):
            self._client_reference = value


        @property
        def pickup(self):
            return self._client_reference
        @pickup.setter
        def pickup(self,value):
            self._client_reference = value


        @property
        def deliverto(self):
            return self._client_reference
        @deliverto.setter
        def deliverto(self,value):
            self._client_reference = value


        @property
        def date_time(self):
            return self._client_reference
        @date_time.setter
        def date_time(self,value):
            self._client_reference = value


        @property
        def event(self):
            return self._client_reference
        @event.setter
        def event(self,value):
            self._client_reference = value


        @property
        def comments(self):
            return self._client_reference
        @comments.setter
        def comments(self,value):
            self._client_reference = value


        @property
        def seal(self):
            return self._client_reference
        @seal.setter
        def seal(self,value):
            self._client_reference = value


        @property
        def safe_yard(self):
            return self._client_reference
        @safe_yard.setter
        def safe_yard(self,value):
            self._client_reference = value

    def send_precapture(self):
        precapture = self._client_reference,self._type_operation,self._unit_truck,self._pickup,self._deliverto,self._internal_reference,self._client
        return precapture
    
class AssignShipmet(Shipment):
    
    def __init__(self,client_reference,type_operation,trailer,unit_truck,internal_reference,client,pickup ,deliverto,*args, **kwargs):
        super(Shipment).__init__(*args, **kwargs)
    
    def PressignShipment(self):
        # para enviar los datos al Db
        pass
    
    def send_precapture(self):
        #extraer los datos del Db
        pass
    
class CaptureTrip(Shipment):
    def __init__(self,client_reference,client, date_time,event,comments,seal,safe_yard,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
    
    def CaptureEvent(self):
        # para enviar los datos a BD
        pass
    
    def extracTrip():
        #para extraer los viajes ya realizados
        pass
    
    def evaluateEvent(self):
        pass