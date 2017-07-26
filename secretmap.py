import numpy as np

class secretmap:
    def __init__(self, row, colm):
        self.map = np.floor(100*np.random.random((row, colm)))
        #print self.map

    #TODO: get rid of stupid function and just codemap.map
    def getmap(self):
        return self.map
