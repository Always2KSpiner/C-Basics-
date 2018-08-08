'''
Created on 18-Jul-2018

@author: anitr
'''
class Box:
    def getVolume(self):
        vol= self.length*self.breadth* self.height
        return vol
    def __init__(self, length, breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height
class BigBox(Box):
    def __init__(self, length, breadth,height):
        Box.__init__(self,length,breadth,height)
    def getCapacity(self, sBox):
        a=super().getVolume()
        b=sBox.getVolume()
        print("Volume of Big Box=",a)
        print("Volume of Small Box=",b)
        print("Capacity is",a/b)
smallbox=Box(1,1,1)
bigbox=BigBox(4,4,4)
capa=bigbox.getCapacity(smallbox)

        