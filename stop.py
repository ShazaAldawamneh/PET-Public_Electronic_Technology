import sys
from battery import Battery

class Stop(object):
    def __init__(self, No:int, No_batteries:int, dist_prev:int, dist_next:int):
        self._No = No
        self._batteries = []
        for i in range(No_batteries):
            self._batteries.append(Battery())
        self._dist_prev = dist_prev
        self._dist_next = dist_next

    def __str__(self):
        battery_list = ""
        for i in self._batteries:
            battery_list += str(i) + ", "
        return str("\tStop number: %d -- Charges: %s -- dist from prev: %s -- dist to next: %s\n" %(self._No, battery_list, self._dist_prev, self._dist_next))

    def swap_battery(self, bus):
        for i in self._batteries:
            if i.charged():
                self._batteries.append(bus.battery)
                bus.battery = i
                self._batteries.remove(i)
                print("Battery Swapped on Bus " + bus)
                return
        sys.exit("No Charged batteries!!!")

    def battery_charge(self, x):
        for i in self._batteries:
            i.increaseCharge(x)

    
            
