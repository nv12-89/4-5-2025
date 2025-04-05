import pgzrun
from random import randint
import time
WIDTH=800
HEIGHT=600
TITLE="Connecting the Satellites"

satellites=[]
lines=[]
next_satellite=0
start_time=0
total_time=0
end_time=0
n=randint(5,10)

for i in range(n):
    s=Actor("satellite_1.png")
    s.pos=randint(50, WIDTH-80), randint(50,HEIGHT-80)
    satellites.append(s)
    start_time=time.time()


def draw():
    global total_time
    screen.blit("spacebg.png",(0,0))
    for i in range (n):
        satellites[i].draw()
        screen.draw.text(str(i+1),(satellites[i].pos[0],satellites[i].pos[1]+20),fontsize=50,color="red")
    
    # for i in satellites:
    #     i.draw() 
    # screen.draw.text(str(i+1),(satellites[i][0],satellites[i][1]),fontsize=50,color="black")
    for i in lines:
        screen.draw.line(i[0],i[1],"cyan")
    
    if next_satellite < n:
        total_time=time.time()-start_time
        # print(time.time())
        screen.draw.text(str(round(total_time,2)),(10,10),fontsize=30)
    
    else:
        screen.draw.text(str(round(total_time,2)),(10,10),fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite < n:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite+=1
        else:
            print(pos)
            lines=[]
            next_satellite=0

pgzrun.go()