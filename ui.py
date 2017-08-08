from algfullmap import MapAlgorithm
from pyglet.window import key
import pyglet
from pyglet.gl import *
from tile import Tile
import numpy as np

def makecircle(xmidpoint,ymidpoint,xradi,yradi):
    PI = 3.1415926535898
    circle_points = 100
    glBegin(GL_LINE_LOOP)
    for i in range(100):
       angle = 2*PI*i/circle_points
       glVertex2f(xmidpoint+np.cos(angle)*yradi, ymidpoint+np.sin(angle)*xradi)

    glEnd()

def pickcolor(value):
    if value > 100: raise Exception

    return [float(value)/100.0, 1.0-float(value)/100.0]

def colorize(themap):
    bigtilearray = []

    rowcount = 0
    count = 0
    ysize = len(themap.secretmap)
    print "ysize: {}".format(ysize)
    for row in themap.secretmap:
        tilearray = []
        for index in row:
            tilearray.append(Tile(x=count, y=ysize-rowcount, colorval=pickcolor(index)))
            count += 1
        bigtilearray.append(tilearray)
        rowcount += 1
        count = 0
    return bigtilearray

#-----------------------------void Main-------------------------------------
virtualmap = MapAlgorithm()
coloredmap = colorize(virtualmap)
edgelist = virtualmap.edges_v2
# findgeometry


window = pyglet.window.Window()

glClearColor(0.0, 0.0, 0.0, 0.0);

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')



# image = pyglet.resource.image('kitten.jpg')
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        print "Window Exited."
        exit(window)

platform = pyglet.window.get_platform()
display = platform.get_default_display()
print display.get_default_screen()


# void reshape (int w, int h)
# {
#    glViewport (0, 0, (GLsizei) w, (GLsizei) h);
#    glMatrixMode (GL_PROJECTION);
#    glLoadIdentity ();
#    gluOrtho2D (0.0, (GLdouble) w, 0.0, (GLdouble) h);
# }

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    #makes color blue
    glColor3f(0.0, 0.0, 1.0)
    #makes color red
    squaresize = 30
    # drawing the map
    for row in coloredmap:
        for i in row:
            glColor3f(i.colorval[0],0.0,i.colorval[1])
            # glColor3f(count,0.0,0.0)
            glBegin(GL_POLYGON)
            glVertex2f(i.location[0]*squaresize+0.0, i.location[1]*squaresize+0.0)
            glVertex2f(i.location[0]*squaresize+0.0, i.location[1]*squaresize+25.0)
            glVertex2f(i.location[0]*squaresize+25.0, i.location[1]*squaresize+25.0)
            glVertex2f(i.location[0]*squaresize+25.0, i.location[1]*squaresize+0.0)
            glEnd()
    glColor3f(0.2, .9, 0.2)
    for element in edgelist:
        print edgelist[element]
        xmidpoint = float(edgelist[element][1]+edgelist[element][3])/2.0
        ymidpoint = float(edgelist[element][2]+edgelist[element][4])/2.0
        xradi = (edgelist[element][3]-edgelist[element][1])/2

        yradi = (edgelist[element][4]-edgelist[element][2])/2
        print "xradi: {}, yradi: {}".format(xradi, yradi)
        print "xmidpoint: {}, ymidpoint: {}".format(xmidpoint, ymidpoint)
        #detect if noise or leak
        if edgelist[element][0] >= 8:
            makecircle(xmidpoint*squaresize+12.5,ymidpoint*squaresize+12.5,xradi*squaresize, yradi*squaresize)
        print element

    # pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    # ('v2i', (10, 15, 30, 35)),
    # ('c3B', (0, 0, 255, 0, 255, 0))
    # )
    # glBegin(GL_TRIANGLES)
    # glVertex2f(0, 0)
    # glVertex2f(window.width, 0)
    # glVertex2f(window.width, window.height)
    # glEnd()

pyglet.app.run()
