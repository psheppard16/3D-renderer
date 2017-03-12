import math
from Display3D.Perspective import *
from Display3D.Rectangle3D import *
from Display3D.Sphere import *
class GameEngine:
    def __init__(self, window):
        self.window = window
        self.mouseDown = False
        self.mouseStartPoint = (0, 0)
        self.rotation = False
        self.translation = False
        self.distance = 1000
        self.angleXP = 0
        self.angleYP = 0
        self.angleZP = 0
        self.perspectiveX = 0
        self.perspectiveY = 0
        self.perspective = Perspective((self.perspectiveX, self.perspectiveY, 0), self.distance, (math.radians(self.angleXP), math.radians(self.angleYP), math.radians(self.angleZP)))
        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0
        self.sphere = Sphere(self.perspective, (300, 0, 0), 100, (0, 0, 0), "red")
        #self.rectangle3D1 = Rectangle3D(self.perspective, (300, 0, 0), (100, 100, 50), (math.radians(self.angleX), math.radians(self.angleY), math.radians(self.angleZ)), "red")
        self.objectList = []

    def runGame(self):
        if self.mouseDown:
            if self.rotation:
                x = self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()
                y = self.window.root.winfo_pointery() - self.window.root.winfo_rooty()
                xChange = x - self.mouseStartPoint[0]
                yChange = y - self.mouseStartPoint[1]
                self.mouseStartPoint = (x, y)
                self.angleXP -= yChange / 2
                self.angleYP -= xChange / 2
            elif self.translation:
                x = self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()
                y = self.window.root.winfo_pointery() - self.window.root.winfo_rooty()
                xChange = x - self.mouseStartPoint[0]
                yChange = y - self.mouseStartPoint[1]
                self.mouseStartPoint = (x, y)
                self.perspectiveX -= xChange 
                self.perspectiveY += yChange
        self.perspective = Perspective((self.perspectiveX, self.perspectiveY, 0), self.distance, (math.radians(self.angleXP), math.radians(self.angleYP), math.radians(self.angleZP)))
        Rectangle3D(self.perspective, (0, 300, 0), (100.0, 100.0, 50.0), (math.radians(self.angleX), math.radians(self.angleY), math.radians(self.angleZ)), "yellow")
        self.sphere = Sphere(self.perspective, (300, 0, 0), 100, (0, 0, 0), "red")

    def kp(self, event):
        if event.char == 'w' or event.char == 'W':
            self.distance += 10
        elif event.char == 's' or event.char == 'S':
            self.distance -= 10
        elif event.char == 'a' or event.char == 'A':
            self.angleX -= 5
        elif event.char == 'd' or event.char == 'D':
            self.angleX += 5
        elif event.char == 'q' or event.char == 'Q':
            self.angleY -= 5
        elif event.char == 'e' or event.char == 'E':
            self.angleY += 5
        elif event.char == 'z' or event.char == 'Z':
            self.angleZ -= 5
        elif event.char == 'c' or event.char == 'C':
            self.angleZ += 5
        elif event.char == 'r' or event.char == 'R':
            self.rotation = True
        elif event.char == 't' or event.char == 'T':
            self.translation = True
        elif event.keysym == 'Left':
            self.angleZP -= 5
        elif event.keysym == 'Right':
            self.angleZP += 5

    def kr(self, event):
        if event.char == 'r' or event.char == 'R':
            self.rotation = False
        elif event.char == 't' or event.char == 'T':
            self.translation = False

    def mousePressed(self, event):
        self.mouseDown = True
        self.mouseStartPoint = (event.x, event.y)

    def mouseReleased(self, event):
        self.mouseDown = False
