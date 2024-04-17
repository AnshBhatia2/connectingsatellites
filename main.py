import pgzrun
from random import randint
import time

WIDTH = 800
HEIGHT = 600
start_time = 0
total_time = 0
end_time = 0

satellites = []
lines = []

next_satellite = 0
number_of_satellites = 8

def create_satellites():
    global start_time
    start_time = time.time()
    for i in range(number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos=(randint(50,750),randint(50,550))

        satellites.append(satellite)

def draw():
    global total_time
    screen.blit("bgsat",(0,0))
    number = 1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        number += 1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    
    if next_satellite < number_of_satellites:
        total_time = time.time() - start_time
        screen.draw.text(str(total_time),(10,10),fontsize=30)

    else:
        screen.draw.text(str(total_time),(10,10),fontsize=30)

def on_mouse_down(pos):
    global next_satellite
    global lines
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append(satellites[next_satellite-1].pos,satellites[next_satellite].pos)
            next_satellite+=1
        else:
            lines=[]
            next_satellite=0




def update():
    pass

pgzrun.go()