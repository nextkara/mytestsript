#!/usr/bin/python
class Person:
    def __init__(self, name, job = 0, pay = 0):
        'version 1.0'
        self.name = name
        self.job = job
        self.pay = pay
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
class Manager(Person):
    def __init__(self):
        'version 1.5.1'
        Person.__init__(self, name, job = 'mgr', pay)
    'version 1.3'
    def giveRaise(self, percent, bonus=.10):
        '''
        'change to good choices --version 1.3.1 '
        self.pay = int(self.pay * (1 + percent + bonus))
        '''
        Person.giveRaise(self, percent + bonus)
    def lastName(self):
        'version 1.4'
        print('This is Manager\'s lastName')
        return self.name.split()[-1]
    def __str__(self):
        'version 1.4.1'
        return '[Manager imformation: %s %s ]' % (self.name, self.pay)
    def giveRaise(self, percent = 0.1):
        'version 1.4.2'
        self.pay = int(self.pay * (1 + percent))

class Department:
    'version 1.5.1--增加了 Department类，'
    def __init__(self, *arg):
        self.members = list(arg)#将输入的元组强制转换为列表
    def addMember(self, person):
        self.members.append(person)#person只是一个形式上的参数，与Person类并没有联系
    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person) 
if __name__ == '__main__':
    bob = Person('Bob Smith',job = 'Cleaner', pay = 500)
    sue = Person('Sue Jones',job = 'Tech', pay = 1000)
    print(bob.name, bob.pay)
    'version 1.1'
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    'version 1.2'
    #tom = Manager('Tom Jonse', job = 'mgr', pay = 2000)
    'version 1.5.1'
    tom = Manager('Tom Jonse', 2000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    'version 1.3'
    print('---All three---')
    for object in (bob, sue, tom):
        object.giveRaise(.10)
        print(object)
    'version 1.4.1'
    'as same as version 1.2 about object tom'    
    'version 1.5.1'
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()
    '''
    version 1.0
    'cut this part'
    print(sue.name, sue.pay)
    sue.pay *= 1.10
    print(sue.pay)
    '''
        