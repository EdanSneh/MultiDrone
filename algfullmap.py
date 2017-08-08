#TODO outline area with highest value and where it tappers off

#initial to do... 3 obvious circles be able to detect themap
#background noise, do not detect that
#merged circle, be able to detect + indentify as merged
#closer circle analysis

from map import themap
import numpy as np

class Mapalgorithm:

    def __init__(self, datamap = themap(14,14)):
        self.datamap = datamap
        self.secretmap = self.datamap.codemap
        self.circlemap = self.detectcircles()
        self.circle_merge(self.circlemap)
        self.map_edges(self.circlemap)

    def map_edges(self, cmap):
        #TODO if inside circle touching outside, map it as part of that circle
        #TODO return array packets of all the different circle numbers ex: c1_in
        for point in self.circles:
            row = point[0]
            col = point[1]
            value = cmap[row][col][0:cmap[row][col].index("_")]

            if row!=len(cmap) and "edge" in cmap[row+1][col]:
                if value not in cmap[row+1][col]: cmap[row+1][col] += ".{}".format(value)
            if col!=0 and "edge" in cmap[row][col-1]:
                if value not in cmap[row][col-1]: cmap[row][col-1] += ".{}".format(value)
            if col!=len(cmap[row]) and "edge" in cmap[row][col+1]:
                if value not in cmap[row][col+1]: cmap[row][col+1] += ".{}".format(value)
            if row!=0 and "edge" in cmap[row-1][col]:
                if value not in cmap[row-1][col]: cmap[row-1][col] += ".{}".format(value)
        # print(cmap)

    def circle_merge(self, cmap):
        self.circles = []
        for row in range(0, len(cmap)):
            for col in range(0, len(cmap[row])):
                if cmap[row][col][0] == "c":
                    #values containing cmap
                    self.circles.append([row, col])
                    index = cmap[row][col]
                    if row!=len(cmap) and cmap[row+1][col][0] == "c" and cmap[row+1][col] != index:
                        self.changeval(thecmap = cmap, initial = cmap[row][col], final = cmap[row+1][col])
                    if col!=0 and cmap[row][col-1][0] == "c" and cmap[row][col-1] != index:
                        self.changeval(thecmap = cmap, initial = cmap[row][col], final = cmap[row][col-1])
                    if col!=len(cmap[row]) and cmap[row][col+1][0] == "c" and cmap[row][col+1] != index:
                        self.changeval(thecmap = cmap, initial = cmap[row][col], final = cmap[row][col+1])
                    if row!=0 and cmap[row-1][col][0] == "c" and cmap[row-1][col] != index:
                        self.changeval(thecmap = cmap, initial = cmap[row][col], final = cmap[row-1][col])

    def changeval(self, thecmap, initial, final):
        for row in range(0, len(thecmap)):
            for col in range(0, len(thecmap[row])):
                if thecmap[row][col] == final:
                    thecmap[row][col] = initial

                # if val == final:
                #     val = initial
                #     print val

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
        return circleit

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

        #create next-array for detecting if val higher than a certain number
