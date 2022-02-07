from battery import Battery
from route import Route

class Bus(object):
    def __init__(self,route, rangeperbattery):
        self._battary = Battery()
        self._route = route
        self._lastStop = 0
        self._distance = 0
        self._rangeperbattery = rangeperbattery
        self._forward = True

    def __str__(self):
        return("Last Bus Stop: %i Distance Travelled From Bus Stop: %i Charge of Battery: %i Range of Battery: %i"% (self._route._stops[self._lastStop]), self._distance, self._battary._charge, self._rangeperbattery)
    
    def incrementDistance(self, distance):
        self._distance += distance 
        self._battary.decreaseCharge(distance/self._rangeperbattery) 
        if self._forward == True:
            distance_to_next_stop = self._route.stops[self._lastStop]._dist_next
        else:
            distance_to_next_stop = self._route.stops[self._lastStop]._dist_prev
        if self._distance >=  distance_to_next_stop:
            self._ArrivedAtNextStop()

    def getDistance(self):
        return self._distance

    def _CanIMakeItToNextStop(self):
        #run to check if possible to make to next stop
        if self._forward == True:
            distance_to_next_stop = self._route.stops[self._lastStop]._dist_next
        else:
            distance_to_next_stop = self._route.stops[self._lastStop]._dist_prev

            if (self._rangeperbattery*self._battary.charge)/100 >= distance_to_next_stop:
                return True 
            else:
            #be sad becuase it doesnt work :(
                return False
    
    def _ArrivedAtNextStop(self):
        self._distance = 0
        if self._forward == True:
            self._lastStop += 1
            if self._route.stops[self._lastStop]._dist_next is None:
                self._forward == False
        else:
            self._lastStop -= 1
            if self._route.stops[self._lastStop]._dist_prev is None:
                self._forward == True

        if self._CanIMakeItToNextStop() == False:
            self._route._stops[self._lastStop].swap_battery
        