#!/usr/bin/python

# Script I found into "Teach your kids to code" a book about python by Bryson Payne all credits reserved to him.

import turtle

colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'gray', 'white', 'pink', 'cyan', 'khaki', 'brown']
iterations=360
rot=59

t=turtle.Pen()
turtle.bgcolor('black')
for x in range(iterations):
    t.pencolor(colors[x%(iterations/rot)])
    t.width(x/100+1)
    t.forward(x)
    t.left(rot)
