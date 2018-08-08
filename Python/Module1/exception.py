'''
Created on 15-Jun-2018

@author: anitr
'''
mylist=[1,2,3,"4",5]
sum=0
for i in mylist:
    try:
        sum+=i
    except TypeError:
        print("Type Error")
print(sum)
try:
    print(mylist[5])
except IndexError:
    print("Index Error Occured")