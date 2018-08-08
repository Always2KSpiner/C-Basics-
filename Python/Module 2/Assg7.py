'''
Created on 29-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
cur.execute("Delete From user1 where userid=1")
cur.execute("Select * from user1")
data=cur.fetchall()
for line in data:
    print(line)
vid=int(input("ENTER VEHICLE ID\n"))     
cur.execute("Delete From vehicle where vehicleid= :var",(vid,))
cur.execute("Select * from vehicle")
data=cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()