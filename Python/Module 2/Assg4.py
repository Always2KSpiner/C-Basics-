'''
Created on 28-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
cur.execute("""Create Table vehicle(
            vehicleid number(5) primary key,
            vehiclename varchar2(10) not null)""")
vid=2001
cur.executemany("""insert into vehicle values(:var1,:var2)""",
                [(vid,'Toyota'),(vid+1,'Maruti'),(vid+2,'Nissan'),(vid+3,'Hyundai')])
cur.executemany("""insert into vehicle values(:par1,:par2)""",
                [{'par1':vid+4,'par2':'Hondaa'},
                 {'par1':vid+5,'par2':'Volkswagen'},
                 ])       
cur.execute("SELECT * From vehicle")
data=cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()