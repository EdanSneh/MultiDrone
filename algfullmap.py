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
        circleit = [[" "]*np.size(self.datamap.map,0) for _ in range(np.size(self.datamap.map,1))]
        self.names = 0
        indexrow = 0
        for row in self.secretmap:
            indexcol = 0
            for rowval in row:
                if rowval < 24:

                    circleit[indexrow][indexcol] = "null"

                elif rowval >= 24 and rowval <= 60:

                    circleit[indexrow][indexcol] = "edge"
                else:
                    sstir = self.namecheck(circleit, indexrow, indexcol)
                    circleit[indexrow][indexcol] = sstir

                indexcol += 1
            indexrow += 1
        print circleit

    def namecheck(self, array, row, col):
        lamebool = False
        if row!=len(array) and array[row+1][col][0] == "c":
            lamebool = True
            savearray = array[row+1][col]
        elif col!=0 and array[row][col-1][0] == "c":
            lamebool = True
            savearray = array[row][col-1]
        elif col!=len(array[row]) and array[row][col+1][0] == "c":
            lamebool = True
            savearray = array[row][col+1]
        elif row!=0 and col!=array[row-1][col][0] == "c":
            lamebool = True
            savearray = array[row-1][col]
        if lamebool:
            return savearray
        self.names += 1
        return "c"+str(self.names)+"_i"
