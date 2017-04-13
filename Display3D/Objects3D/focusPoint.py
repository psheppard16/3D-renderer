import math
from Display3D.Objects3D.object3D import Object3D
from Display3D.Objects3D.pyramid3D import Pyramid3D
from Display3D.Objects3D.rectangle3D import Rectangle3D
import Display3D.util3D as util3D
class FocusPoint(Object3D):
    def __init__(self, perspective, location, angles):
        super().__init__(perspective, location=location, angles=angles)
        self.perspective = perspective
        self.focusSize = 2.5
        self.rectangle3D1 = Rectangle3D(self.perspective, (location[0] + self.focusSize * 11, location[1] + 0, location[2] + 0), (self.focusSize * 6, self.focusSize, self.focusSize), (0, 0, 0), (255, 0, 0))
        self.pyramid3D1 = Pyramid3D(self.perspective, (location[0] + self.focusSize * 22, location[1] + 0, location[2] + 0), (self.focusSize * 2, self.focusSize * 2, self.focusSize * 2), (0, 0, math.pi / 2), (255, 0, 0))
        self.rectangle3D2 = Rectangle3D(self.perspective, (location[0] + 0, location[1] + self.focusSize * 11, location[2] + 0), (self.focusSize, self.focusSize * 6, self.focusSize), (0, 0, 0), (0, 0, 255))
        self.pyramid3D2 = Pyramid3D(self.perspective, (location[0] + 0, location[1] + self.focusSize * 22, location[2] + 0), (self.focusSize * 2, self.focusSize * 2, self.focusSize * 2), (0, 0, 0), (0, 0, 255))
        self.rectangle3D3 = Rectangle3D(self.perspective, (location[0] + 0, location[1] + 0, location[2] + self.focusSize * 11), (self.focusSize, self.focusSize, self.focusSize * 6), (0, 0, 0), (0, 255, 0))
        self.pyramid3D3 = Pyramid3D(self.perspective, (location[0] + 0, location[1] + 0, location[2] + self.focusSize * 22), (self.focusSize * 2, self.focusSize * 2, self.focusSize * 2), (-math.pi / 2, 0, 0), (0, 255, 0))
        self.rectangle3D4 = Rectangle3D(self.perspective, (location[0] + 0, location[1] + 0, location[2] + 0), (self.focusSize, self.focusSize, self.focusSize), (0, 0, 0), (0, 0, 0))

    def getSides(self):
        return self.rectangle3D1.getSides() + \
        self.rectangle3D2.getSides() + \
        self.rectangle3D3.getSides() + \
        self.rectangle3D4.getSides() + \
        self.pyramid3D1.getSides() + \
        self.pyramid3D2.getSides() + \
        self.pyramid3D3.getSides()

    def setLocation(self, location):
        self.location = location
        self.rectangle3D1.setLocation((self.location[0] + self.focusSize * 11, self.location[1] + 0, self.location[2] + 0))
        self.pyramid3D1.setLocation((self.location[0] + self.focusSize * 22, self.location[1] + 0, self.location[2] + 0))
        self.rectangle3D2.setLocation((self.location[0] + 0, self.location[1] + self.focusSize * 11, self.location[2] + 0))
        self.pyramid3D2.setLocation((self.location[0] + 0, self.location[1] + self.focusSize * 22, self.location[2] + 0))
        self.rectangle3D3.setLocation((self.location[0] + 0, self.location[1] + 0, self.location[2] + self.focusSize * 11))
        self.pyramid3D3.setLocation((self.location[0] + 0, self.location[1] + 0, self.location[2] + self.focusSize * 22))
        self.rectangle3D4.setLocation((self.location[0] + 0, self.location[1] + 0, self.location[2] + 0))

    def setAngle(self, angles):
        self.angles = angles
        self.rectangle3D1.setAngle(self.angles)
        self.pyramid3D1.setAngle(self.angles + math.pi / 2)
        self.rectangle3D2.setAngle(self.angles)
        self.pyramid3D2.setAngle(self.angles)
        self.rectangle3D3.setAngle(self.angles)
        self.pyramid3D3.setAngle(self.angles - math.pi / 2)
        self.rectangle3D4.setAngle(self.angles)

    def move(self, vector):
        self.location = util3D.add_v3v3(self.location, vector)
        self.rectangle3D1.move(vector)
        self.pyramid3D1.move(vector)
        self.rectangle3D2.move(vector)
        self.pyramid3D2.move(vector)
        self.rectangle3D3.move(vector)
        self.pyramid3D3.move(vector)
        self.rectangle3D4.move(vector)

    def changeAngle(self, angles):
        self.angles = util3D.add_v3v3(self.angles, angles)
        self.rectangle3D1.changeAngle(angles)
        self.pyramid3D1.changeAngle(angles)
        self.rectangle3D2.changeAngle(angles)
        self.pyramid3D2.changeAngle(angles)
        self.rectangle3D3.changeAngle(angles)
        self.pyramid3D3.changeAngle(angles)
        self.rectangle3D4.changeAngle(angles)