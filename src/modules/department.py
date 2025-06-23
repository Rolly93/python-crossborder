from employee import Employee
class Department(Employee): 
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        pass


class Capturista(Department):
    def __init__(self) :   
        self._department = "Capturista" 
        self._username =  userName
        super().__init__(self._department)
        
        def assignTrip (self):
            
            
            pass
        
        def captureTrip(self,):
            
            
            pass
        
        def moveFalse(self):
            pass
        
        @property
        def userName (self):
            return self._username
        
        @userName.setter
        def userName (self, email):
            self._username = userName
    
class Transfer (Department):
    def __init__(self, *args, **kwargs):
        self._department = "Transfer"
        self._precCanture = preCapture
        self._userCapture = userCapture

        super().__init__( self._department,*args, **kwargs)
        
        @property
        def preCapture(self):
            return self._precCanture
        
        @preCapture.setter
        def preCapture (self, preCapture):
            self._precCanture = preCapture
        @property
        def userCapture(self):
            return self._userCapture
        
        @userCapture.setter
        def userCapture (self,userCapture):
            self._userCapture = userCapture    


