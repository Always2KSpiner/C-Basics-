'''
Created on 15-Jun-2018

@author: anitr
'''
lis=[]
lis2=[]
dic={}
i=0
f=open("C:\\Users\\anitr\\Desktop\\student_details.txt","r+")
for line in f:
    temp=line.split()
    i+=1
    lis.append(temp)
    dic[line]=i
print(lis)
lis2.append(dic)
print(lis2)
f.close()
