from Display3D.Rectangle3D import *
from Display3D.Pyramid3D import *
import math
class FocusPoint:
    def __init__(self, perspective, location):
        self.perspective = perspective
        self.location = location
        focusSize = 2.5
        self.rectangle3D1 = Rectangle3D(self.perspective, (location[0] + focusSize * 11, location[1] + 0, location[2] + 0), (focusSize * 6, focusSize, focusSize), (0, 0, 0), "red")
        self.pyramidD3 = Pyramid3D(self.perspective, (location[0] + focusSize * 22, location[1] + 0, location[2] + 0), (focusSize * 2, focusSize * 2, focusSize * 2), (0, 0, math.pi / 2), "red")
        self.rectangle3D2 = Rectangle3D(self.perspective, (location[0] + 0, location[1] + focusSize * 11, location[2] + 0), (focusSize, focusSize * 6, focusSize), (0, 0, 0), "blue")
        self.pyramidD3 = Pyramid3D(self.perspective, (location[0] + 0, location[1] + focusSize * 22, location[2] + 0), (focusSize * 2, focusSize * 2, focusSize * 2), (0, 0, 0), "blue")
        self.rectangle3D3 = Rectangle3D(self.perspective, (location[0] + 0, location[1] + 0, location[2] + focusSize * 11), (focusSize, focusSize, focusSize * 6), (0, 0, 0), "green")
        self.pyramidD3 = Pyramid3D(self.perspective, (location[0] + 0, location[1] + 0, location[2] + focusSize * 22), (focusSize * 2, focusSize * 2, focusSize * 2), (-math.pi / 2, 0, 0), "green")
        self.rectangle3D3 = Rectangle3D(self.perspective, (location[0] + 0, location[1] + 0, location[2] + 0), (focusSize, focusSize, focusSize), (0, 0, 0), "black")



