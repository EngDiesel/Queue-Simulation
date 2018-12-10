import random

class Customer(object):
    def __init__(self, arrivalTime=0, serviceBegin=0):
        self.id = 1
        self.interArrival = random.randint(1, 5)
        self.arrivalTime = arrivalTime
        self.serviceBegin = serviceBegin
        self.serviceDuration = random.randint(1, 5)
        self.serviceEnds = self.serviceBegin + self.serviceDuration
