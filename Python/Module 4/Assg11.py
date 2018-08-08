'''
Created on 17-Jul-2018

@author: anitr
'''
class Book:
    def __init__(self,title,author,publisher):
        self.title = title
        self.auth = author
        self.pub = publisher
    def __str__(self):
            return self.title+" "+self.auth+" "+self.pub 
b=Book("Percy","Rick Riordan","Penguin")
print(b)