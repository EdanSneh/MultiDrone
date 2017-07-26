from map import themap
from secretmap import secretmap

class algorithm:
    def __init__(self):
        peakfound = False
        highestval = -1

        datamap = themap(7, 7)
        highesttuple = [datamap.measure(), datamap.x, datamap.y]
        #print datamap

        while(peakfound == False):
            if datamap.x > 0:
                datamap.left()
            else:
                break;
            plot = datamap.measure()
            if plot > highestval : highestval = [plot, datamap.x, datamap.y]
        print highestval

    def smartestmove():
        """calculates where drone should move to"""
        topeak()
        nearpeak()
        awaypeak()
        brainlessmove()

    def topeak():
        if abs(datamap.x-highestval[1]) < abs(datamap.y-highestval[2]):
            x=3
            return True
        return False
    def nearpeak():

    def awaypeak():

    def brainlessmove():
        #moveleft
        if datamap.x > 0 and datamap.map[datamap.y][datamap.x-1] == None:
            datamap.left()
