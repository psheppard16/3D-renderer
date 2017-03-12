from Display3D.RenderFrame import *
from Display3D.FocusPoint import *
class Perspective:
    def __init__(self, focusLocation, distance, angles):
        self.objectList = []
        self.angles = angles
        self.distance = distance
        self.focusLocation = focusLocation
        self.focusPoint = FocusPoint(self, self.focusLocation)
        self.location = (focusLocation[0], focusLocation[1], focusLocation[2] + self.distance)
        self.renderFrame = RenderFrame(self, (focusLocation[0], focusLocation[1], focusLocation[2] + self.distance - 1000), (0, 0, 1))

    def isInFrame(self, point):
        if point[2] <= self.location[2]:
            return True
        else:
            return False