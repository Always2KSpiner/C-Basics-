'''
Created on 18-Jul-2018

@author: anitr
'''
class calculator:
    def __init__(self):
        pass
    @staticmethod
    def isprime(num):
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    return False
                    break  
                else:  
                    return True  
        else:  
            return False
    def nextprime(self):
        for i in range(0,50):
            if(calculator.isprime(i)):
                print(i)
cal=calculator()
print(cal.nextprime())

