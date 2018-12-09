import random
from model import Customer

customers = []

# Manually Generate The first 'Customer' with completely random values.
customers.append(Customer())
customers[0].interArrival = None

# this loop generates 9 other 'Customers' and appends them to 'customers' list.
for i in range(1, 10):
    new = Customer()

    _arrivalTime = customers[i-1].arrivalTime + new.interArrival
    _serviceBegin = max(customers[i-1].serviceEnds, _arrivalTime)
    _serviceEnd = _serviceBegin + new.serviceDuration

    new.arrivalTime = _arrivalTime
    new.serviceBegin = _serviceBegin
    new.serviceEnds = _serviceEnd

    customers.append(new)


for customer in customers:
    print "interArrival => " + str(customer.interArrival) + \
     "\t| arrivalTime => " + str(customer.arrivalTime) +\
     "\t| Service Begin => " + str(customer.serviceBegin) +\
     "\t| Service Duration => " + str(customer.serviceDuration) +\
     "\t| Service End => " + str(customer.serviceEnds)
