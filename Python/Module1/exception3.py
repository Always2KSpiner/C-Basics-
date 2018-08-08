'''
Created on 15-Jun-2018

@author: anitr
'''
try:
    num=int(input("ENTER NUMBER\n"))
except:
    print("ERROR!!!\nENTER A NATURAL NUMBER ONLY")
else:
    x=0
    sum=0
    while x<=num:
        sum+=x
        x+=1
    print("SUM IS ",sum)

