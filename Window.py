__author__ = 'psheppard16'
from FrameRate import *
from MainMenu import *
from Instructions import *
from DrawingEngine import *
from Options import *
from GameEngine import *
class Window:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.cMenu = "null"
        self.rMenu = "mainMenu"
        self.root = tk.Tk()
        self.root.title("Sizable Board")
        self.root.bind('<KeyPress>', self.kp)
        self.root.bind('<KeyRelease>', self.kr)
        self.root.bind("<Button-1>", self.mousePressed)
        self.root.bind("<ButtonRelease-1>", self.mouseReleased)
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.scale = .95
        self.requestedScale = .95
        self.frameRate = FrameRate(self)
        self.mainMenu = MainMenu(self)
        self.instructions = Instructions(self)
        self.gameEngine = GameEngine(self)
        self.drawingEngine = DrawingEngine(self)
        self.options = Options(self)
        self.root.after(1, self.loop)
        self.root.mainloop()

    def loop(self):
        while True:
            if self.frameRate.getTime() > self.frameRate.nextTick:
                self.frameRate.tickStartTime = self.frameRate.getTime()
                self.frameRate.nextTick += self.frameRate.TICK_SPEED
                self.width = self.root.winfo_width()
                self.height = self.root.winfo_height()
                self.updateFrameSizes()
                if(str(self.root.winfo_screenwidth()) + "x" +  str(self.root.winfo_screenheight()) != self.options.resolution.get()):
                    self.root.geometry(self.options.resolution.get())
                    self.root.update()
                if self.cMenu != self.rMenu:
                    self.clearWindow()
                    if self.rMenu == "instructions":
                        self.instructions.f.pack(side=LEFT)
                    if self.rMenu == "options":
                        self.options.f.pack(side=LEFT)
                    if self.rMenu == "mainMenu":
                        self.mainMenu.f.pack(side=LEFT)
                    if self.rMenu == "gameEngine":
                        self.gameEngine = GameEngine(self)
                        self.drawingEngine.f.pack(side=LEFT)
                        self.lastFrameCalc = int(self.frameRate.getTime())
                    self.cMenu = self.rMenu
                if self.cMenu == "gameEngine":
                    self.gameEngine.runGame()
                    self.frameRate.startTimer("display")
                    self.drawingEngine.render(self.gameEngine.perspective.renderFrame.renderPolygons(self.gameEngine.perspective.objectList))
                    self.frameRate.timeChange()
                    self.frameRate.update()

    def kp(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.kp(event)

    def kr(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.kr(event)

    def mousePressed(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.mousePressed(event)

    def mouseReleased(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.mouseReleased(event)

    def clearWindow(self):
        self.options.hide()
        self.instructions.hide()
        self.drawingEngine.hide()
        self.mainMenu.hide()

    def updateFrameSizes(self):
        self.options.f.config(width=self.width, height =self.width)
        self.instructions.f.config(width=self.width, height =self.width)
        self.mainMenu.f.config(width=self.width, height =self.width)
        self.drawingEngine.f.config(width=self.width, height =self.width)
