import time as t

class StopWatch :

    def __init__(self):
        self.start = t.time()
        self.end = t.time()

    def getStarTime(self):
        return self.start

    def getEndTime(self):
        return self.end

    def Start(self):
        self.start = t.time()

    def Stop(self):
        self.end = t.time()

    def getElapsedTime(self):
        return (self.getEndTime() - self.getStarTime())*1000