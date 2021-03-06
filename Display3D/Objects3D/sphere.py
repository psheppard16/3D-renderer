from Display3D.Objects3D.object3D import Object3D
import Display3D.util3D as util3D
from Display3D.polygon import Polygon
import math
class Sphere(Object3D):
    def __init__(self, perspective, location, radius, angles, color):
        super().__init__(perspective, location=location, angles=angles)
        self.color = color
        self.perspective = perspective
        self.perspective.objectList.append(self)
        self.location = location
        self.radius = radius
        self.angles = angles
        self.RESOLUTION = 10 #must be even

    def update(self, perspective, location, radius, angles, color):
        self.color = color
        self.perspective = perspective
        self.location = location
        self.radius = radius
        self.angles = angles

    def getSides(self):
        points = []
        for zAngle in range(self.RESOLUTION):
            for yAngle in range(self.RESOLUTION):
                point = util3D.multiAxisRotation((self.radius, 0, 0), (0, math.radians(yAngle * 360 / self.RESOLUTION), math.radians(zAngle * 360 / self.RESOLUTION)))
                point = util3D.multiAxisRotation(point, self.angles)
                point = self.addLocation(point)
                point = util3D.multiAxisRotation(point, self.perspective.angles)
                point = self.addFocusPoint(point)
                points.append(point)

        sides = []
        for j in range(self.RESOLUTION - 1):
            for i in range(self.RESOLUTION - 1):
                side = []
                side.append(points[i + j * self.RESOLUTION])
                side.append(points[i + j * self.RESOLUTION + 1])
                side.append(points[i + (j + 1) * self.RESOLUTION + 1])
                side.append(points[i + (j + 1) * self.RESOLUTION])
                sides.append(side)

        side = [] #a side is missed by the side generation algorithm
        side.append(points[self.RESOLUTION + (self.RESOLUTION - 2) * self.RESOLUTION - self.RESOLUTION * (int(self.RESOLUTION / 2 - 1)) - 1])
        side.append(points[self.RESOLUTION + (self.RESOLUTION - 3) * self.RESOLUTION - self.RESOLUTION * (int(self.RESOLUTION / 2 - 1))])
        side.append(points[self.RESOLUTION + (self.RESOLUTION - 2) * self.RESOLUTION - self.RESOLUTION * (int(self.RESOLUTION / 2 - 1))])
        side.append(points[self.RESOLUTION + (self.RESOLUTION - 1) * self.RESOLUTION - self.RESOLUTION * (int(self.RESOLUTION / 2 - 1)) - 1])
        sides.append(side)

        polygons = []
        for side in sides:
            polygons.append(Polygon(side, self.color))

        return polygons