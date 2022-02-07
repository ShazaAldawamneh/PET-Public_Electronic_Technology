class Battery(object):
    def __init__(self):
        self._charge = 100  

    def __str__(self):
        return str(self._charge)   

    def getCharge(self):
        return self._charge

    def setCharge(self, charge): #get the charge from outside the function 
        self._charge= charge
        
    charge = property(getCharge, setCharge)

    def charged(self): 
        if self._charge >= 75:
            return True
        else:
            return False

    def increaseCharge(self,x): #dont let it get over 100
        if self._charge == 100:
            return
        if 100 - self.charge < x:
            self._charge = 100
        self._charge += x

    def decreaseCharge(self,x): #dont let it go below 0
        if self._charge == 0:
            return
        if self._charge-x  < 0:
            self._charge = 100
        self._charge -= x
