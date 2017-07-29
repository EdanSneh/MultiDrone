#TODO outline area with highest value and where it tappers off

#initial to do... 3 obvious circles be able to detect themap
#background noise, do not detect that
#merged circle, be able to detect + indentify as merged
#closer circle analysis

from map import themap
import numpy as np

class mapalgorithm:

    def __init__(self, datamap = themap(14,14)):
        self.datamap = datamap
        self.secretmap = self.datamap.codemap
        circlemap = self.detectcircles()

    def detectcircles(self):
        #TODO array not using strs
        circleit = [[""]*np.size(self.datamap.map,0) for _ in range(np.size(self.datamap.map,1))]

        indexrow = 0
        for row in self.secretmap:
            indexcol = 0
            for rowval in row:
                if rowval < 24:
                    circleit[indexrow][indexcol] = "null"
                    self.namecheck()
                elif rowval >= 24 and rowval <= 60:
                    self.namecheck()
                    circleit[indexrow][indexcol] = "c1_ex"
                else:
                    circleit[indexrow][indexcol] = "c1_in"
                print circleit
                indexcol += 1
            indexrow += 1
