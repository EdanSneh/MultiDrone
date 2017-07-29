import numpy as np
from secretmap import secretmap

class themap():
    def __init__(self, row, colm):
        if row <= 0 or colm <= 0 : raise ValueError

        self.row = row
        self.colm = colm
        self.y = (row-1)/2
        self.x = (colm-1)/2

        self.map = np.empty((row, colm))
        self.map[:] = np.NAN
        #print self.map

        self.codemap = secretmap(row, colm).map
    def append(self, row, colm, value):
        self.map[row][colm] = value
        #print self.map



    def measure(self):
        self.map[self.y][self.x] = self.codemap.map[self.y][self.x]
        print "PTCH level: {} at [{}, {}]".format(self.map[self.y][self.x], self.x+1, self.y+1)
        print self.map
        return self.map[self.y][self.x]

    def left(self):
        if self.x == 0: raise ValueError
        self.x += -1

    def right(self):
        if self.x == self.colm: raise ValueError
        self.x += 1

    def up(self):
        if self.y == 0: raise ValueError
        self.y += -1

    def down(self):
        if self.y == self.row: raise ValueError
        self.y += 1

    def __str__(self):
        self.printmap()
        return ""
    def printmap(self):
        print self.map
