import time as tm
import random
import money

class NorthAmerican:
    class Canadian:
        class Person:
            def __init__(self, id, firstName, lastName):
                self.id = id
                self.fname = firstName
                self.lname = lastName
                self.age = 0
                self.hungry = False
                self.sleep = False
            def grow(self):
                tm.sleep(86400)
                self.age += 1 
            def asleep(self):
                tm.sleep(149)
                self.sleep = True
                tm.sleep(88)
                self.sleep = False
            def getHungry(self):
                if self.sleep == False:
                    tm.sleep(49)
                    self.hungry = True
                    tm.sleep(1.5)
                    self.hungry = False
                else:
                    tm.sleep()

        class Employee(Person):
            def __init__(self, name, salary):
                self.name = name
                self.sal = None

        class Teacher(Employee):
            def __init__(self, name):
                self.name = name
                self.sal = money.cad(46524)

        class ContrusctionWorker(Employee):
            def __init__(self, name):
                self.name = name

    class American:
        class Person:
            def __init__(self, id, firstName, lastName):
                self.id = id
                self.fname = firstName
                self.lname = lastName
                self.age = 0
                self.hungry = False
                self.sleep = False
            def grow(self):
                tm.sleep(86400)
                self.age += 1 
            def asleep(self):
                tm.sleep(149)
                self.sleep = True
                tm.sleep(88)
                self.sleep = False
            def getHungry(self):
                if self.sleep == False:
                    tm.sleep(49)
                    self.hungry = True
                    tm.sleep(1.5)
                    self.hungry = False
                else:
                    tm.sleep()

        class Employee(Person):
            def __init__(self, name, salary):
                self.name = name
                self.sal = None

        class Teacher(Employee):
            def __init__(self, name):
                self.name = name
                self.sal = money.cad(46524)

        class ContrusctionWorker(Employee):
            def __init__(self, name):
                self.name = name
