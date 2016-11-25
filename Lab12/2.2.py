__author__ = 'los16dura'
class Mother:
    age  = 0
    status = ''
    name = ''
    def __init__(self, name, age ):
        self.age = age
        self.name = name
        #self.status = status
    def __str__(self):
       return 'Hello, my name is ' + self.name +' I,m ' + str(self.age)

class Daughter(Mother):
    def __str__(self):
        return 'Hello, my name is ' + self.name +' I,m ' + str(self.age) + 'years old'

m = Mother( 'Olga' ,33)
d = Daughter( 'Julia' , 16)
print(m)
print(d)