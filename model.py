import random, json

class Customer(object):
    def __init__(self, arrivalTime=0, serviceBegin=0):
        self.id = 1
        self.points = []
        self.interArrival = random.randint(1, 10)
        self.arrivalTime = arrivalTime
        self.serviceBegin = serviceBegin
        self.serviceDuration = random.randint(1, 5)
        self.serviceEnds = self.serviceBegin + self.serviceDuration

        start = self.arrivalTime
        end = self.serviceEnds
        for i in range(start, end):
            obj = {
                "x" : str(i),
                "y" : 1
            }
            self.points.append(obj)

    @property
    def getPoints(self):
        return str(json.dumps(self.points))
