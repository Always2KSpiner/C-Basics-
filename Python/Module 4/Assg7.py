'''
Created on 17-Jul-2018

@author: anitr
'''
class Dog:
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks=trick
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.name,d.tricks)
print(e.name,e.tricks)
