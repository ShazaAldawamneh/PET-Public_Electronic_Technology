# bus battery = 120 Kwh  ---- as tesla 3 has 83 kwh
# avarge discharge = 1.65Kwh/km  ---- from real world eletric bus testing
# discharge ratio  120/1.65 = 72.72km range per battery

# set variables
from route import Route
from stop import Stop
from bus import Bus

battery_capacity = 300 # bus battery = 120 Kwh  ---- as tesla 3 has 83 kwh
discharge_rate = 1.65 # avarge discharge = 1.65Kwh/km  ---- from real world eletric bus testing
range_per_battery = battery_capacity/discharge_rate # discharge ratio  120/1.65 = 72.72km range per battery
range_per_battery_in_m = range_per_battery * 100

batteries_per_stop = 3

speed_of_sim = 100

# set the scene // describe routes
lemon = Route("lemon", [Stop(234, batteries_per_stop, None, 634), Stop(236, batteries_per_stop, 632, 1232), Stop(238, batteries_per_stop, 1232, 763), Stop(240, batteries_per_stop, 763, None)])
#print(lemon)

# assign busses routes
bus1 = Bus(lemon, range_per_battery_in_m)
#print(bus1)

# run simulation
# for i in range(100):
#     bus1.incrementDistance(speed_of_sim)
