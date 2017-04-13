import Display3D.util3D as util3D
from Display3D.Objects3D.focusPoint import FocusPoint
from Display3D.renderFrame import RenderFrame
class Perspective:
    def __init__(self, focusLocation, distance, angles):
        self.objectList = []
        self.angles = angles
        self.distance = distance
        self.focusLocation = focusLocation
        self.location = (focusLocation[0], focusLocation[1], focusLocation[2] + self.distance)
        self.renderFrame = RenderFrame(self, (focusLocation[0], focusLocation[1], focusLocation[2] + self.distance - 1000), (0, 0, 1))
        self.focusPoint = FocusPoint(self, focusLocation, self.angles)
        self.hidden = False

    def update(self):
        self.location = (self.focusLocation[0], self.focusLocation[1], self.focusLocation[2] + self.distance)
        self.renderFrame = RenderFrame(self, (self.focusLocation[0], self.focusLocation[1], self.focusLocation[2] + self.distance - 1000), (0, 0, 1))
        self.focusPoint.setLocation(self.focusLocation)

    def showfocus(self):
        if self.focusLocation not in self.objectList:
            self.objectList.append(self.focusLocation)

    def hideFocus(self):
        if self.focusLocation in self.objectList:
            self.objectList.remove(self.focusLocation)

    def isInFrame(self, point):
        return True

    def setFocusLocation(self, location):
        self.focusPoint.setLocation(location)
        self.focusLocation = location

    def setAngle(self, angles):
        self.angles = angles

    def setDistance(self, distance):
        self.distance = distance

    def move(self, vector):
        self.location = util3D.add_v3v3(self.location, vector)
        self.focusLocation = util3D.add_v3v3(self.location, (0, 0, -self.distance))

    def changeAngle(self, angles):
        self.angles = util3D.add_v3v3(self.angles, angles)

    def changeDistance(self, change):
        self.distance += change
        self.location = (self.focusLocation[0], self.focusLocation[1], self.focusLocation[2] + self.distance)