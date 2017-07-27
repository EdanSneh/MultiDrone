import numpy as np
from map import themap
from secretmap import secretmap

class algorithm:

    def __init__(self):
        peakfound = False

        global datamap
        datamap = themap(7, 7)
        global highesttuple
        highesttuple = [-1, datamap.x, datamap.y]
        #print datamap
        while(peakfound == False):
            move = self.smartestmove()
            print move
            break;
            plot = datamap.measure()
            if plot > highesttuple : highesttuple = [plot, datamap.x, datamap.y]
        print highesttuple

    def smartestmove(self):
        """calculates where drone should move to"""

        positions = self.availiblemoves()
        if abs(datamap.x-highesttuple[1]) == abs(datamap.y- highesttuple[2]) : return self.brainlessmove(positions)
        shorterdistance = self.xory()
        lastmove = self.nochoice(positions)
        if lastmove>1:
            return lastmove
        order = self.queue(highesttuple, shorterdistance)
        return self.whereto(positions, order)



    def queue(self, highesttuple, shorter):
        priority = [0,0,0,0]
        if shorter:
            if datamap.y > highesttuple[2]:
                priotity[3]=1
                priority[2]=4
            else:
                priority[3]=4
                priority[2]=1

            if datamap.x > highesttuple[1]:
                priority[1] = 3
                priority[0] = 2
            else:
                priority[1] = 2
                priority[0] = 3
        else:
            if datamap.x > highesttuple[1]:
                priority[1] = 4
                priority[0] = 1
            else:
                priority[1] = 1
                priority[0] = 4
            if datamap.y > highesttuple[2]:
                priotity[3] = 2
                priority[2] = 3
            else:
                priority[3] = 3
                priority[2] = 2
        return priority




    def nochoice(self, plist):
        count = 1
        if sum(plist) == 1:
            for i in plist:
                if i == 1:
                    return count
                count+= 1
        return 0


    def availiblemoves(self):
        positions = [0,0,0,0]
        #left
        if np.isnan(datamap.map[datamap.y][datamap.x-1]):
            positions[0] = 1
        #right
        if np.isnan(datamap.map[datamap.y][datamap.x+1]):
            positions[1] = 1
        #up
        if np.isnan(datamap.map[datamap.y+1][datamap.x]):
            positions[2] = 1
        #down
        if np.isnan(datamap.map[datamap.y-1][datamap.x]):
            positions[3] = 1
        return positions

    def xory(self):
        """
        True if distance to X larger
        False if distance to Y larger
        """
        if abs(datamap.x-highesttuple[1]) < abs(datamap.y-highesttuple[2]):
            return False
        return True
    def brainlessmove(self, plist):
        count = 1
        for i in plist:
            if i == 1:
                return count
            count+=1
        #stuck in middle fix algorithm
        print "dumb stuck"
        raise ValueError

    def whereto(self, plist, olist):
        counter = 0
        bestmove = 5
        for i in plist:
            if i == 1:
                if olist[counter]<bestmove:
                    bestmove = olist[counter]
                    bestmoveindex = counter+1
            counter+=1
        return bestmoveindex
