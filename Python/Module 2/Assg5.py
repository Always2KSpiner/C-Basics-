'''
Created on 29-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()      
cur.execute("SELECT * From user1 where userid=4")
data=cur.fetchall()
for line in data:
    print(line)
cur.execute("UPDATE user1 set username= :var1 , usertype= :var2 where userid=4",{'var1':"lookingforjob@yahoo.com",'var2':"Jobseeker"})
cur.execute("SELECT * From user1 where userid=4")
data=cur.fetchall()
for line in data:
    print(line)
cur.execute("SELECT * From user1 where userid=1")
data=cur.fetchall()
for line in data:
    print(line)
psw=input("ENTER NEW PASSWORD(USER 1)\n")
cur.execute("UPDATE user1 set password= :par1 where userid=1",{'par1':psw})
cur.execute("SELECT * From user1 where userid=1")
data=cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()