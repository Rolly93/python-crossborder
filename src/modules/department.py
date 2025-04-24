from employee import Employee
class Department(Employee): 
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        pass


class Capturista(Department):
    def __init__(self) :   
        self._department = "Capturista" 
        self._email =  email
        super().__init__(self._department)
        
        def assignTrip (self):
            
            
            pass
        
        def captureTrip(self,):
            
            
            pass
        
        def moveFalse(self):
            pass
        
        @property
        def email (self):
            return self._email
        @email.setter
        def email (self, email):
            self._email = email
    
class Transfer (Department):
    def __init__(self, firstname, lastname, garden, employeeId, *args, **kwargs):
        self._department = "Transfer"
        super().__init__(firstname, lastname, garden, employeeId, self._department,*args, **kwargs)
        
        pass
    


