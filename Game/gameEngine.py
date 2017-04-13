__author__ = 'Preston Sheppard'
import math

from Display3D.Objects3D.rectangle3D import *
from Display3D.Objects3D.sphere import *
from Display3D.perspective import *


class GameEngine:
    def __init__(self, game):
        self.game = game

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
        self.perspectiveZ = 0
        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0
        self.perspective = Perspective((self.perspectiveX, self.perspectiveY, self.perspectiveZ), self.distance, (math.radians(self.angleXP), math.radians(self.angleYP), math.radians(self.angleZP)))
        self.box = Rectangle3D(self.perspective, (0, 300, 0), (100.0, 100.0, 50.0), (math.radians(self.angleX), math.radians(self.angleY), math.radians(self.angleZ)), (0, 255, 255))
        #self.sphere = Sphere(self.perspective, (300, 0, 0), 100, (0, 0, 0), (255, 0, 0))


    def run(self):
        if self.mouseDown:
            if self.rotation:
                x = self.game.window.root.winfo_pointerx() - self.game.window.root.winfo_rootx()
                y = self.game.window.root.winfo_pointery() - self.game.window.root.winfo_rooty()
                xChange = x - self.mouseStartPoint[0]
                yChange = y - self.mouseStartPoint[1]
                self.mouseStartPoint = (x, y)
                self.angleXP -= yChange / 2
                self.angleYP -= xChange / 2
            elif self.translation:
                x = self.game.window.root.winfo_pointerx() - self.game.window.root.winfo_rootx()
                y = self.game.window.root.winfo_pointery() - self.game.window.root.winfo_rooty()
                xChange = x - self.mouseStartPoint[0]
                yChange = y - self.mouseStartPoint[1]
                self.mouseStartPoint = (x, y)
                self.perspectiveX -= xChange
                self.perspectiveY += yChange
        self.perspective.setFocusLocation((self.perspectiveX, self.perspectiveY, self.perspectiveZ))
        self.perspective.setDistance(self.distance)
        self.perspective.setAngle((math.radians(self.angleXP), math.radians(self.angleYP), math.radians(self.angleZP)))
        self.perspective.update()
        #self.game.frameRateEngine.printDiagnostics()

    def keyPressed(self, event):
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

    def keyReleased(self, event):
        if event.char == 'r' or event.char == 'R':
            self.rotation = False
        elif event.char == 't' or event.char == 'T':
            self.translation = False

    def mousePressed(self, event):
        self.mouseDown = True
        self.mouseStartPoint = (event.x, event.y)

    def mouseReleased(self, event):
        self.mouseDown = False





