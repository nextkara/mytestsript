#!/usr/bin/python
class Person:
    def __init__(self, name, job = 0, pay = 0):
        'version 1.0'
        self.name = name
        self.job = job
        self.pay = pay

class Manager(Person):
    'version 1.3'
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus))
    
    def lastName(self):
        'version 1.1'
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        'version 1.1'
        self.pay = int(self.pay * (1 + percent))
        
    def __str__(self):
        'version 1.2'
        'fix a error in this part--version 1.2.1'
        return '[Person : %s %s ]' % (self.name, self.pay)
    
    if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones',job = 'Tech', pay = 1000)
        print(bob.name, bob.pay)
        'version 1.1'
        print(bob.lastName(), sue.lastName())
        sue.giveRaise(.10)
        print(sue.pay)
        '''
        version 1.0
        'cut this part'
        print(sue.name, sue.pay)
        sue.pay *= 1.10
        print(sue.pay)
        '''
        