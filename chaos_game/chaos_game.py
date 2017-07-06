#!/usr/bin/python

# I was inspired by this video https://www.youtube.com/watch?v=kbKtFN71Lfs

import os
import sys
import json
import getopt
import random

import turtle

colors=['red', 'green', 'blue', 'purple', 'yellow', 'orange', 'gray', 'white', 'pink', 'cyan', 'khaki', 'brown']

# init Turtle
w=turtle.Screen()
t=turtle.Pen()
turtle.bgcolor('black')
t.pensize(1)
t.penup()

width, height = w.screensize()
# print str(width)
# print str(height)

# n: for number of seeds.
# r: for the ratio about how much to move.
# c: when new points are needed to be generated, they'll be part of a convex polygon.
# remaining args will be for the firsts the points representing the seeds and
# the last one be the first random point (coords separated by ':').
# Every missing point will created randomly according to the previous parameters.
# If only one point is given this will be the first point to draw and not the seeds.
optlist, args = getopt.getopt(sys.argv[1:], 'n:i:r:c')
# print str(optlist)
# print str(args)
# init options
number_of_seeds = 3
ratio = float(1)/float(2)
iterations = 360
convex = False
for o, a in optlist:
    if o in ('-n', '--number_of_seeds'):
        number_of_seeds = int(a)
    elif o in ('-r', '--ratio'):
        t_a = a.split('/')
        if len(t_a) == 1:
            ratio = a
        elif len(t_a) == 2:
            ratio = float(t_a[0]) / float(t_a[1])
        else:
            raise
    elif o in ('-i', '--iterations'):
        iterations = a
    elif o in ('-c', '--convex'):
        convex = True
# print str(number_of_seeds)
# print str(ratio)
# print str(iterations)
# print str(convex)

# format options and complete missing options
seeds = [[int(y) for y in x.split(':')] for x in args[0:-1]]
first_point = [[int(y) for y in x.split(':')] for x in args[-1:]]
if len(first_point):
    first_point = first_point[0]
# print str(seeds)
# print str(first_point)
while len(seeds) < number_of_seeds:
    seeds.append([random.randint(-width, width), random.randint(-height, height)])
if not len(first_point):
    first_point = [random.randint(-width, width), random.randint(-height, height)]
# print str(seeds)
# print str(first_point)

# draw seeds
t.pencolor(colors[0])
for x, y in seeds:
    # print 'x: ', str(x), 'y: ', str(y)
    t.goto(x, y)
    t.dot()

# draw first point
t.pencolor(colors[1])
t.goto(first_point[0], first_point[1])
t.dot()

# draw shape
t.pencolor(colors[2])
current_point = first_point
for i in range(iterations):
    seed = seeds[random.randint(0, len(seeds) - 1)]
    # print str(seed)
    # print str(current_point)
    # print str('=')
    current_point = [(seed[0] + current_point[0]) * ratio, (seed[1] + current_point[1]) * ratio]
    # print str(current_point), "\n"
    t.goto(current_point[0], current_point[1])
    t.dot()

w.exitonclick()
