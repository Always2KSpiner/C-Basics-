'''
Created on 15-Jun-2018

@author: anitr
'''
f=open("C:\\Users\\anitr\\Desktop\\testfile1.txt","r+")
data = f.read()
print(data)
f1=open("C:\\Users\\anitr\\Desktop\\testfile2.txt","w+")
f1.write(data.replace('\"', '\\\"')) 
f1.close()
f.close()
f2=open("C:\\Users\\anitr\\Desktop\\testfile2.txt","r+")
data2=f2.read()
print(data2)
f2.close()