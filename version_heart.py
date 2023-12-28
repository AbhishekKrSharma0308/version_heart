import math
from turtle import*
speed(0)
bgcolor("black")

def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 13*math.cos(k)-5*math.cos(2*k)-math.cos(3*k)-math.cos(4*k)

for i in range(600):
    goto(hearta(i)*20,heartb(i)*20)
    color('red')
    for j in range(5):
        goto(0,0)