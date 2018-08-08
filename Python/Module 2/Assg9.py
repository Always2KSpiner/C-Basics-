'''
Created on 30-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
try:
    cur.execute("Delete from user1 where user_id=2")
except cx_Oracle.DatabaseError as e:
    print(e)
id='rahulitsme@gmaill.com'
try:
    cur.execute("Delete from user1 where username=:var",{'var':id})
except:
    print("ERROR")
try:
    cur.execute("select * from user")
except cx_Oracle.DatabaseError as f:
    print(f)
else:
    data=cur.fetchall()
    for line in data:
        print(line)
    con.commit()
con.close()