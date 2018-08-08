'''
Created on 17-Jul-2018

@author: anitr
'''
class Store:
    __item_count = 100
    def __init__(self):
        pass
    @classmethod
    def addItem(cls,count):
        cls.__item_count+=count
    @classmethod
    def issueItem(cls,count):
        cls.__item_count-=count
    @classmethod
    def getItemCount(cls):
        print(cls.__item_count)
counter1 = Store()
counter2 = Store()
counter1.addItem(2)
counter1.issueItem(1)
Store.getItemCount()

    