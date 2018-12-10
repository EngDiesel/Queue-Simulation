import random
from model import Customer
from flask import Flask

from flask import Flask
from flask import url_for
from flask import render_template
import json

app = Flask(__name__)


@app.route("/test")
def test():
    obj = []
    for i in range(15, 20):
        obj.append(i)

    return str(obj)


@app.route('/')
def main():
    customers = []
    # Manually Generate The first 'Customer' with completely random values.
    customers.append(Customer())
    customers[0].interArrival = None
    customers[0].state = "In Service"

    # this loop generates 4 other 'Customers' and appends them to 'customers' list.
    for i in range(1, 8):
        new = Customer()
        _arrivalTime = customers[i-1].arrivalTime + new.interArrival
        _serviceBegin = max(customers[i-1].serviceEnds, _arrivalTime)
        _serviceEnd = _serviceBegin + new.serviceDuration

        new.arrivalTime = _arrivalTime
        new.serviceBegin = _serviceBegin
        new.serviceEnds = _serviceEnd
        new.id = i + 1

        # check for the customer state.
        if new.arrivalTime < new.serviceBegin:
            new.state = new.serviceBegin - new.arrivalTime
        else:
            new.state = 0

        customers.append(new)
        """
        for customer in customers:
            print "interArrival => " + str(customer.interArrival) + \
             "\t| arrivalTime => " + str(customer.arrivalTime) +\
             "\t| Service Begin => " + str(customer.serviceBegin) +\
             "\t| Service Duration => " + str(customer.serviceDuration) +\
             "\t| Service End => " + str(customer.serviceEnds)
        """
    for cust in customers:
        cust.points = []
        start = cust.arrivalTime
        end = cust.serviceEnds
        for i in range(start, end):
            obj = {
                "x" : i + 1,
                "y" : 1
            }
            cust.points.append(obj)

    return render_template('index.html', customers=customers)


def printCustomers():
    for customer in customers:
        print "interArrival => " + str(customer.interArrival) + \
         "\t| arrivalTime => " + str(customer.arrivalTime) +\
         "\t| Service Begin => " + str(customer.serviceBegin) +\
         "\t| Service Duration => " + str(customer.serviceDuration) +\
         "\t| Service End => " + str(customer.serviceEnds)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
