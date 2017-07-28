#TODO outline area with highest value and where it tappers off

#initial to do... 3 obvious circles be able to detect themap
#background noise, do not detect that
#merged circle, be able to detect + indentify as merged
#closer circle analysis

from map import themap
class mapalgorithm:

    def __init__(self):
        self.datamap = themap(10,10)
        self.secretmap = self.datamap.codemap
        print self.datamap
