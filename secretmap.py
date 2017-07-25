import numpy as np

class secretmap:
    def __init__(self, row, colm):
        self.map = np.floor(100*np.random.random((row, colm)))
        print self.map
