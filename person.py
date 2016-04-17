#!/usr/bin/python
from classtool import AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
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
    '''
    version 1.5.4 drop this functon :)
    def __str__(self):
        'version 1.2'
        'fix a error in this part--version 1.2.1'
        return '[Person : %s %s ]' % (self.name, self.pay)
   '''
class Manager(Person):
    '''
    这里存在问题，作为嵌入模块的话，之后的类方法的引用方式要修改--;fixed it
    '''
    def __init__(self, name, pay):
        '''
        'version 1.5.1'#输入变量的时候存在问题 job = 'mgr'
        Person.__init__(self, name, job = 'mgr', pay)
        '''
        'version 1.5.2'
        Person.__init__(self, name, 'mgr', pay)
    '''
    version 1.5.4 drop these functons :)
    'version 1.3'
    def giveRaise(self, percent, bonus=.10):
        'change to good choices --version 1.3.1 '
        self.pay = int(self.pay * (1 + percent + bonus))
        Person.giveRaise(self, percent + bonus)
    def lastName(self):
        'version 1.4'
        print('This is Manager\'s lastName')
        return self.name.split()[-1]
    def __str__(self):
        'version 1.4.1'
        return '[Manager imformation: %s %s ]' % (self.name, self.pay)
    def giveRaise(self, percent = 0.05):
        'version 1.4.2'
        self.pay = int(self.pay * (1 + percent))
    '''
'''
version 1.5.4 drop this class :)    
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
'''
if __name__ == '__main__':
    bob = Person('Bob Smith',job = 'Cleaner', pay = 500)
    sue = Person('Sue Jones',job = 'Tech', pay = 1000)
    #print(bob.name, bob.pay)
    'version 1.1'
    
    
    print(sue)
    print(bob)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    #print(sue.pay)
    'version 1.2'
    #tom = Manager('Tom Jonse', job = 'mgr', pay = 2000)
    'version 1.5.1'
    tom = Manager('Tom Jonse', 2000)
    #tom.giveRaise(.10)没有修改加薪比例，自动赋值为0.05的加薪比例，为Manager特有的定制方法
    tom.giveRaise(0.10)
    print(tom.lastName())
    print(tom)
    'version 1.3'
    print('---All Imformation---')#change three to Imformation :) version 1.5.3
    for object in (bob, sue, tom):
        object.giveRaise(.10)
        print(object)
    'version 1.4.1'
    'as same as version 1.2 about object tom'    
    '''
    drop in version 1.5.4
    'version 1.5.1'
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()
    '''
    '''
    version 1.0
    'cut this part'
    print(sue.name, sue.pay)
    sue.pay *= 1.10
    print(sue.pay)
    ---first run---
    Bob Smith 500
    Smith Jones
    1100
    This is Manager's lastName
    Jonse
    [Manager imformation: Tom Jonse 0 ]
    ---All three---
    [Person : Bob Smith 550 ]
    [Person : Sue Jones 1210 ]
    [Manager imformation: Tom Jonse 0 ]
    [Person : Bob Smith 605 ]
    [Person : Sue Jones 1331 ]
    [Manager imformation: Tom Jonse 0 ]
    -------
    ---second run---
    Bob Smith 500
    Smith Jones
    1100
    This is Manager's lastName
    Jonse
    [Manager imformation: Tom Jonse 2200 ]
    ---All three---
    [Person : Bob Smith 550 ]
    [Person : Sue Jones 1210 ]
    [Manager imformation: Tom Jonse 2420 ]
    [Person : Bob Smith 605 ]
    [Person : Sue Jones 1331 ]
    [Manager imformation: Tom Jonse 2662 ]
    -------
    
    '''
    