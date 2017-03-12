__author__ = 'psheppard16'
import time
class FrameRate:
    def __init__(self, window):
        self.window = window
        self.VARIABLE_FRAMERATE = True
        self.UPDATE_TIME = .25
        self.nextFrameCalc = 0
        self.tickSum = 0
        self.tickStartTime = 0
        self.renderTime = 1 / 20
        self.renderedFrame = True
        self.requestedFrameRate = 1 / 30
        self.nextTick = 0
        self.TICK_SPEED = 1 / 30
        self.loadTime = 1
        self.time = 0
        self.startTime = 0
        self.longestTaskTime = 0
        self.longestTask = "null"

    def update(self):
        self.TICK_SPEED = self.getTime() - self.nextTick
        self.loadTime -= self.TICK_SPEED

    def getTime(self):
        self.time = time.clock()
        return self.time

    def startTimer(self, task):
        self.startTime = self.getTime()
        self.task = task

    def timeChange(self):
        timeChange = self.getTime() - self.startTime
        if timeChange > self.longestTaskTime:
            self.longestTask = self.task
            self.longestTaskTime = timeChange

    def getLongestTask(self):
        #if self.longestTaskTime != 0:
            #print("frame rate:", str(1 / self.TICK_SPEED))
            #print("Longest task:", self.longestTask, "Percent:", str(self.longestTaskTime / self.TICK_SPEED * 100) + "%" , "Time:", str(self.longestTaskTime))
        #if self.longestTask == "runBlob":
        #    print(len(self.window.gameEngine.blobList) / self.longestTaskTime)
        self.longestTask = "null"
        self.longestTaskTime = 0