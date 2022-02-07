class Route(object):

    def __init__(self, name:str, stop_list:list):
        self._name = name
        self._stops = stop_list

    def __str__(self):
        returnString = "Route " + self._name + " :\n"
        for i in self.stops:
            returnString += str(i)
        return returnString

    def get_stops(self):
        return self._stops

    stops = property(get_stops)

    
