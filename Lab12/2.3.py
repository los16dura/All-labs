__author__ = 'los16dura'
class Animals:
    age  = 0
    name = ''
    kind = ''
    def __init__(self, name, age ):
        self.age = age
        self.name = name
    def __str__(self):
       return 'Hello, my name is ' + self.name +' I,m ' + str(self.age) + ' years old'
class Dolphin(Animals):
    pass
class Zebra(Animals):
    pass
d = Dolphin( 'Lucky' ,3)
z = Zebra( 'Melman' , 7)
print(z)
print(d)
