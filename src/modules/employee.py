import re
import email
import phonenumbers

class Employee:
    def __init__(self,*args, **kwargs):

        self._employeeId=employeeId
        self._firstname = firstname
        self._lastname = lastname 
        self._phonenumber= phonenumber
        self._cellphone= cellphone
        #self._charge=charge
        #I Must let this pending // self._btday = btday
        self._street = street
        self._city=city
        self._estado=estado
        self._garden = garden
        
        @property
        def garden(self):
            return self._garden
        @garden.setter
        def garden(self, value):
            self._garden = value
        
        @property
        def employeeId(self):
            return self._employeeId
        
        @employeeId.setter
        def employeeId(self, value):
            self._employeeId = value
        
       # @property
       # def charge(self):
       #     return self._charge
       # 
       # @charge.setter
       # def charge(self, value):
       #     self._charge = value
        
        
        @property
        def street(self):
            return self._street
        @street.setter
        def street(self, value):
            self._street = value
        
        @property
        def estado(self):
            return self._estado
        @estado.setter
        def estado(self, value):
            self._estado = valid_string(value,"estado")
        
        
        
        @property
        def city(self):
            return self._city
        @city.setter
        def city(self, value):
            self._city = valid_string(value,"ciudad")
        
        @property
        def phonenumber(self):
            return self._phoneNumber
        
        @phonenumber.setter
        def phonenumber(self,value):
            self._phoneNumber = validate_Number(value,'phone number')
        
        
        @property 
        def cellphone(self):
            return self._cellPhone
        @cellphone.setter
        def cellphone(self,value):
            self._cellPhone = validate_Number(value,'cellphone number')
        
        
        @property
        def lastname(self):
            return self._lastname
        
        @lastname.setter
        def lastname(self, value):
            self._lastname = valid_string(value, "lastaname")
        
        
        @property
        def firstname(self):
            return self._firstname
        
        @firstname.setter
        def firstname(self, value):
            self._firstname = valid_string(value,"fisrtname")
            
        
        
        #to validate strigns on name
        def valid_string (string , fieldname):
           pattern = r"^[a-zA-Z\s'-]+$"
           valid_name = bool(re.fullmatch(pattern,string))
           if valid_name:
               return string
           else:
            raise ValueError(f"Invalid {fieldname}: Please use only letters, spaces, hyphens, and apostrophes.")
        #to validate a any cellphone or phonenumber
        def validate_Number(number, fieldNumber):
            pars_number = phonenumbers.parse(number)
            if phonenumbers.is_valid_number(pars_number):
                return number
            else:
                raise ValueError (f"Invalid {fieldNumber}: Please use a valid number")