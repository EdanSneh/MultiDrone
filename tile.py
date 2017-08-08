
class Tile:

    def __init__(self, x, y, colorval):
        self.colorval = colorval
        self.location = [x, y]

    def __str__(self):
        return str(self.colorval[0])
