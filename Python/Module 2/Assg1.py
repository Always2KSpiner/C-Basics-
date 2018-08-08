'''
Created on 26-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
cur.execute("SELECT * From employer")
print(cur.fetchall())
print(cur.rowcount)
print(cur.description)
con.close()