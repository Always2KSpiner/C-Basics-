dic={}
dic2={}
i,count=0,0
f=open("C:\\Users\\anitr\\Desktop\\rhyme.txt","r+")
f1=open("C:\\Users\\anitr\\Desktop\\words.txt","w+")
for line in f:
    for temp in line.split():
        i+=1
        dic[temp]=i
        temp=temp.lower()
        dic2[temp]=i
f1.write("TOTAL NO. OF WORDS: "+str(i)+"\n")
f1.write(str(dic)+"\n")
f1.write("UNIQUE WORDS: "+str(len(dic2))+"\n")
for x in dic2:
    f1.write(x+"\n")
f.close()
f1.close()
f3=open("C:\\Users\\anitr\\Desktop\\words.txt","r+")
print(f3.read())
f3.close()

