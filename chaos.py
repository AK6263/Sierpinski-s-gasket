# -*- coding: utf-8 -*-
"""

@author: Abhay Kshirsagar
"""

import turtle
import math
import random
a=turtle.Turtle()
wn =turtle.Screen()
a.shape('blank')
wn.bgcolor('black')
a.color('white')
sc=a.getscreen()
a.speed(0)
x,y = [0.0,216.51,-216.51],[250.0,-125.0,-125.0]


def ranpt(b,c):
    a = random.randint(0,2)
    p,q = int(x[a]),int(y[a])
    b = (b+p)*0.5
    c = (c + q)*0.5
    return b,c
    
def start():
    for i,j in zip(x,y):
        a.up()
        a.goto(i,j)
        a.down()
        a.dot()
    
    d1,d2 = 0,0
    i=0
    while i<10000:
        a.up()
        a.goto(d1,d2)
        #print(d1,d2)
        d1,d2 = ranpt(d1,d2)
        a.down()
        a.dot(size=2.5) 
        i+=1

if __name__ == "__main__":
    start()
