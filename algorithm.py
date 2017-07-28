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
        counter = 0

        while(peakfound == False):
            plot = datamap.measure()
            if plot > highesttuple[0] : highesttuple = [plot, datamap.x, datamap.y]
            move = self.smartestmove()
            self.executemove(move)
            counter+=1
        print highesttuple

    def executemove(self, move):
        if move == 1:
            datamap.left()
            return
        elif move == 2:
            datamap.right()
            return
        elif move == 3:
            datamap.up()
            return
        elif move == 4:
            datamap.down()
            return
        raise ValueError



    def smartestmove(self):
        """calculates where drone should move to"""

        positions = self.availiblemoves()
        print datamap.x
        print highesttuple[1]
        print "boolean {}".format(abs(datamap.x-highesttuple[1]))
        print "boolean {}".format(abs(datamap.y-highesttuple[2]))
        if abs(datamap.x-highesttuple[1]) == 0 and abs(datamap.y-highesttuple[2]) == 0: return self.brainlessmove(positions)
        shorterdistance = self.xory()
        lastmove = self.nochoice(positions)
        if lastmove>1:
            return lastmove
        order = self.queue(highesttuple, shorterdistance)
        return self.whereto(positions, order)



    def queue(self, highesttuple, shorter):
        priority = [0,0,0,0]
        #distance to y is shorter
        if shorter:
            if datamap.y > highesttuple[2]:
                priority[3]=4
                priority[2]=1
            else:
                priority[3]=1
                priority[2]=4

            if datamap.x > highesttuple[1]:
                priority[1] = 3
                priority[0] = 2
            else:
                priority[1] = 2
                priority[0] = 3
        #distance to x is shorter
        else:
            if datamap.x > highesttuple[1]:
                priority[1] = 4
                priority[0] = 1
            else:
                priority[1] = 1
                priority[0] = 4
            if datamap.y > highesttuple[2]:
                priority[3] = 3
                priority[2] = 2
            else:
                priority[3] = 2
                priority[2] = 3
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
        if datamap.x!=0 and np.isnan(datamap.map[datamap.y][datamap.x-1]):
            positions[0] = 1
        #right
        if datamap.x!=datamap.colm-1 and np.isnan(datamap.map[datamap.y][datamap.x+1]):
            positions[1] = 1
        #up
        if datamap.y!=0 and np.isnan(datamap.map[datamap.y-1][datamap.x]):
            positions[2] = 1
        #down
        if datamap.y!=datamap.row-1 and np.isnan(datamap.map[datamap.y+1][datamap.x]) :
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
        print "brainlessmove:"
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
                print olist
                if olist[counter]<bestmove:
                    bestmove = olist[counter]
                    bestmoveindex = counter+1
            counter+=1
        return bestmoveindex
