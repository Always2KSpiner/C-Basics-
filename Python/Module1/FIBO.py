'''
Created on 15-Jun-2018

@author: anitr
'''
def fibo(number):
    if(number == 0):
        return (0)
    elif(number == 1):
        return (1)
    else: 
        return fibo(number - 1) + fibo(number - 2)
num=int(input("ENTER NUMBER"))
if num<0:
    print("ENTER VALID INPUT")
else:
    for i in range(num):
        print(fibo(i))      
