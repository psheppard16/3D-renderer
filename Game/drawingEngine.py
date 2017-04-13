__author__ = 'Preston Sheppard'
from FrameWork.Display.canvasObject import CanvasObject
try:
    import pygame
except:
    pass
class DrawingEngine(CanvasObject):
    def __init__(self, game):
        #Drawing engine is a child of CanvasObject,
        #which contains the drawing methods for canvas
        super().__init__(game)

        self.game = game
        self.setBackgroundColor((255, 255, 255))
        self.setDrawLayer(50)


    def getScreenX(self, x):
        return x

    def getScreenY(self, y):
        return self.game.window.height - y

    def draw(self):
        xShift = self.game.window.width / 2
        yShift = self.game.window.height / 2
        renderedPolygons = self.game.gameEngine.perspective.renderFrame.renderPolygons(self.game.gameEngine.perspective.objectList)
        for polygon in renderedPolygons:
            self.showPolygon(polygon.points, polygon.color, position=(xShift, yShift), shiftPosition=True, width=3)

