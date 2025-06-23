class Truck():
    def __init__(self, unittruck,Plates):
        self.unittruck = unittruck
        self.Plates = Plates
        self.enable = None
        pass
    
    def disable (self,value):
        if  str(value).lower() is not "no":
            self.enable = True
        else:
            self.enable = False