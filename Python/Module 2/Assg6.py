'''
Created on 29-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()      
print("OLD TABLE")
cur.execute("SELECT * From vehicle")
data=cur.fetchall()
for line in data:
    print(line)
oldid=2001
newid=1001
for line in data:
    cur.execute("update vehicle set vehicleid= :var1 where vehicleid= :var2",{'var1':newid,'var2':oldid})
    oldid+=1
    newid+=1
cur.execute("update vehicle set vehiclename='Mahindra' where vehicleid=1003")
print("\nUPDATED TABLE")
cur.execute("SELECT * From vehicle")
data=cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()