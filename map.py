from tkinter import *
from threading import Thread
from time import sleep

from main import lemon

def updateWindow():
    window.update()

def displayDimensions(x, y):
    print(f'({x}, {y})')

window = Tk()
window.title('Satellite')
window.iconbitmap('hackathon2022/bus.ico')
window.geometry('1000x700')

full_map = Canvas(window, bg='#f7f6dc', width=window.winfo_screenwidth(), height=window.winfo_screenheight())
full_map.pack()
updateWindow()
window_centerX = round(window.winfo_width() * 0.5)
window_centerY = round(window.winfo_height() * 0.5)

bus_hub = full_map.create_oval(window_centerX - 50, window_centerY - 50, window_centerX + 50, window_centerY + 50, fill='#000')

# bus settings
BUS_ROUTE = 7 # 0-7
BUS_SPEED = 50 # numbers should divide into 200 with no remainders



# diagonal routes
DIAGONAL_LENGTH = 250

route1 = full_map.create_line(window_centerX - DIAGONAL_LENGTH, window_centerY - DIAGONAL_LENGTH, window_centerX + DIAGONAL_LENGTH, window_centerY + DIAGONAL_LENGTH, fill='#000', width=10)

route2 = full_map.create_line(window_centerX - DIAGONAL_LENGTH, window_centerY + DIAGONAL_LENGTH, window_centerX + DIAGONAL_LENGTH, window_centerY - DIAGONAL_LENGTH, fill='#000', width=10)

# straight routes
STRAIGHT_LENGTH = 300

route3 = full_map.create_line(window_centerX - STRAIGHT_LENGTH, window_centerY, window_centerX + STRAIGHT_LENGTH, window_centerY, fill='#000', width=10)

route4 = full_map.create_line(window_centerX, window_centerY - STRAIGHT_LENGTH, window_centerX, window_centerY + STRAIGHT_LENGTH, fill='#000', width=10)

# stops
STOPS_SIZE = 10
STOPS_INBETWEEN_DISTANCE = 50

stops = lemon.get_stops()

def generateStops(stopsArray, route:int):
    straight_routes = [0, 2, 4, 6]
    diagonal_routes = [1, 3, 5, 7]

    if route in straight_routes:
        if route == 0:
            current_posX = window_centerX + 20
            current_posY = window_centerY - 100

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')
                current_posY -= STOPS_INBETWEEN_DISTANCE

        elif route == 2:
            current_posX = window_centerX + 100
            current_posY = window_centerY + 20

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')
                current_posX += STOPS_INBETWEEN_DISTANCE

        elif route == 4:
            current_posX = window_centerX + 20
            current_posY = window_centerY + 100

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')
                current_posY += STOPS_INBETWEEN_DISTANCE

        else:
            current_posX = window_centerX - 100
            current_posY = window_centerY + 20

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')
                current_posX -= STOPS_INBETWEEN_DISTANCE

    else:
        if route == 1:
            current_posX = window_centerX + 100
            current_posY = window_centerY - 70

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')

                current_posX += STOPS_INBETWEEN_DISTANCE
                current_posY -= STOPS_INBETWEEN_DISTANCE

        elif route == 3:
            current_posX = window_centerX + 100
            current_posY = window_centerY + 70

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')

                current_posX += STOPS_INBETWEEN_DISTANCE
                current_posY += STOPS_INBETWEEN_DISTANCE

        elif route == 5:
            current_posX = window_centerX - 100
            current_posY = window_centerY + 50

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')

                current_posX -= STOPS_INBETWEEN_DISTANCE
                current_posY += STOPS_INBETWEEN_DISTANCE

        else:
            current_posX = window_centerX - 100
            current_posY = window_centerY - 50

            for _ in range(len(stopsArray)):
                full_map.create_oval(current_posX, current_posY, current_posX + STOPS_SIZE, current_posY + STOPS_SIZE, fill='red', outline='red')

                current_posX -= STOPS_INBETWEEN_DISTANCE
                current_posY -= STOPS_INBETWEEN_DISTANCE

generateStops(stops, BUS_ROUTE)



# buses
busIcon = PhotoImage(file='hackathon2022/bus32.png')

def moveBusT(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, 0, speed)
    else:
        full_map.move(bus, 0, -speed)

def moveBusB(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, 0, -speed)
    else:
        full_map.move(bus, 0, speed)

def moveBusL(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, speed, 0)
    else:
        full_map.move(bus, -speed, 0)

def moveBusR(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, -speed, 0)
    else:
        full_map.move(bus, speed, 0)

def moveBusDTL(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, speed, speed)
    else:
        full_map.move(bus, -speed, -speed)

def moveBusDBL(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, speed, -speed)
    else:
        full_map.move(bus, -speed, speed)

def moveBusDTR(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, -speed, speed)
    else:
        full_map.move(bus, speed, -speed)

def moveBusDBR(bus, speed, goBack = False):
    if goBack:
        full_map.move(bus, -speed, -speed)
    else:
        full_map.move(bus, speed, speed)




class Bus:
    def __init__(self, bus, speed, route):
        self.bus = bus
        self.speed = speed
        self.route = route

        self.routeDirections = [moveBusT, moveBusDTR, moveBusR, moveBusDBR, moveBusB, moveBusDBL, moveBusL, moveBusDTL]
        self.routeDirectionsLength = [STRAIGHT_LENGTH, DIAGONAL_LENGTH, STRAIGHT_LENGTH, DIAGONAL_LENGTH, STRAIGHT_LENGTH, DIAGONAL_LENGTH, STRAIGHT_LENGTH, DIAGONAL_LENGTH]

    def move(self):
        # forward
        for _ in range(round(self.routeDirectionsLength[self.route] / self.speed)):
            sleep(1)
            self.routeDirections[self.route](self.bus ,self.speed)

        # backward
        for _ in range(round(self.routeDirectionsLength[self.route] / self.speed)):
            sleep(1)
            self.routeDirections[self.route](self.bus ,self.speed, True)




bus = Bus(full_map.create_image(window_centerX, window_centerY, image=busIcon), BUS_SPEED, BUS_ROUTE)

movementThread = Thread(target=bus.move)
movementThread.setDaemon(True)
movementThread.start()

window.mainloop()