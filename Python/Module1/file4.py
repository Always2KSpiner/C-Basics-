'''
Created on 15-Jun-2018

@author: anitr
'''
lis=[]
dic={}
i=0
f=open("C:\\Users\\anitr\\Desktop\\course.txt","r+")
for line in f:
    i+=1
    lis.append(line)
    dic[line]=i
print(lis)
print(dic)
f.close()
