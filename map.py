import numpy as np


class themap():
    def __init__(self, row, colm):
        if row <= 0 or colm <= 0 : raise ValueError

        self.row = row
        self.colm = colm
        self.x = (row-1)/2
        self.y = (colm-1)/2

        self.map = np.empty((self.row, self.colm))
        self.map[:] = np.NAN
        print self.map

    def append(self, row, colm, value):
        self.map[row][colm] = value
        print self.map

    def measure(self):
        print "PTCH level: {}".format(self.map[self.x][self.y])
        return self.map[self.x][self.y]

    def left(self):
        if self.x == 0: raise ValueError
        self.x += -1

    def right(self):
        if self.x == self.colm: raise ValueError
        self.x += 1

    def up(self):
        if self.y == 0: raise ValueError
        self.y += 1

    def down(self):
        if self.y == self.row: raise ValueError
        self.y += -1
