'''
Created on 01-Jul-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
try:
    cur.execute("INSERT INTO product VALUES('P106','Jams',150)")
except cx_Oracle.DatabaseError as e:
    print("ERROR OCUURED\n",e,"\nINSERTING DEFAULT VALUE 0")
    cur.execute("INSERT INTO product VALUES('P106','Jams',150,0)")
cur.execute("Select * from product")
data=cur.fetchall()
for line in data:
    print(line)
con.close()