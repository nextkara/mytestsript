#!/usr/bin/python
from person import Person, Manager
bob = Person('Bob Smith',job = 'Cleaner', pay = 500)
sue = Person('Sue Jones',job = 'Tech', pay = 1000)
tom = Manager('Tom Jonse', 2000)

import shelve
db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()