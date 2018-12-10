import random
from model import Customer
from flask import Flask

from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    customers = []
    # Manually Generate The first 'Customer' with completely random values.
    customers.append(Customer())
    customers[0].interArrival = None

    # this loop generates 9 other 'Customers' and appends them to 'customers' list.
    for i in range(1, 5):
        new = Customer()

        _arrivalTime = customers[i-1].arrivalTime + new.interArrival
        _serviceBegin = max(customers[i-1].serviceEnds, _arrivalTime)
        _serviceEnd = _serviceBegin + new.serviceDuration

        new.arrivalTime = _arrivalTime
        new.serviceBegin = _serviceBegin
        new.serviceEnds = _serviceEnd
        new.id = i + 1

        customers.append(new)


    for customer in customers:
        print "interArrival => " + str(customer.interArrival) + \
         "\t| arrivalTime => " + str(customer.arrivalTime) +\
         "\t| Service Begin => " + str(customer.serviceBegin) +\
         "\t| Service Duration => " + str(customer.serviceDuration) +\
         "\t| Service End => " + str(customer.serviceEnds)

    return render_template('index.html', customers=customers)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
