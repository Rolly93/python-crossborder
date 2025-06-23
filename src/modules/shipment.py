
class Shipment():
    
    def __init__(self,clientReference,client,internalReference,operation,origen,deliverTo,trailerNumber,seal, *args, **kwargs):
        self._client_reference = clientReference 
        self._client=client 
        self._internal_reference= internalReference 
        self._type_operation = operation 
        self._pickup  = origen 
        self._deliverto = deliverTo 
        self._trailer = trailerNumber 
        self._seal= seal
        self._unit_truck=None #unidad
        self._date_time = None
        self._event=None
        self._comments = None
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
    
    def PreCature(self):
        myNewData = self._client_reference,self._client,self._internal_reference,self._type_operation,self._pickup,self._deliverto,self._trailer,self._seal
        #here ill send the data to db
        print("Informacion Capturada \n",myNewData)
        
        pass
    
    def AssgingShipemt(sefl):
        pass
    
    def SearchShipment(sefl):
        pass
    
    def GetData(sefl):
        pass
    
    def DeleteShipment(sefl):
        pass
    
    def UpDateShipment(sefl):
        pass