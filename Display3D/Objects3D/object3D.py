__author__ = 'Preston Sheppard'
import Display3D.util3D as util3D
from abc import ABCMeta, abstractmethod
class Object3D(metaclass=ABCMeta):
    def __init__(self, perspective, location=(0,0,0), angles=(0,0,0)):
        self.perspective = perspective
        self.perspective.objectList.append(self)
        self.location = location
        self.angles = angles
        #import is called on init to avoid circular imports
        from Display3D.perspective import Perspective

        #formatting errors
        if not isinstance(perspective, Perspective):
            raise Exception(str(perspective) + " is not an instance of the class Perspective. You must provide a perspective object")

    def addLocation(self, point):
        x = point[0] - self.perspective.focusLocation[0] + self.location[0]
        y = point[1] - self.perspective.focusLocation[1] + self.location[1]
        z = point[2] - self.perspective.focusLocation[2] + self.location[2]
        return (x, y, z)

    def addFocusPoint(self, point):
        x = point[0] + self.perspective.focusLocation[0]
        y = point[1] + self.perspective.focusLocation[1]
        z = point[2] + self.perspective.focusLocation[2]
        return (x, y, z)

    def setLocation(self, location):
        self.location = location

    def setAngle(self, angles):
        self.angles = angles

    def move(self, vector):
        self.location = util3D.add_v3v3(self.location, vector)

    def changeAngle(self, angles):
        self.angles = util3D.add_v3v3(self.angles, angles)

    @abstractmethod
    def getSides(self):
        pass