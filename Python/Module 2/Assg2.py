'''
Created on 28-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
cur.execute("""SELECT emailid From employer where industrytype='IT' and city='Bangalore'""")
print(cur.fetchall())
status='Active'
cit=input("ENTER CITY\n")
cur.execute("""SELECT companyname,mobile,emailid From employer 
where renewalstatus= :param1 and city= :param2 """,(status,cit))
print(cur.fetchall())
cur.execute("""SELECT companyname,mobile,emailid From employer
where renewalstatus= :param1 and city= :param2 """,(cit,status))
print(cur.fetchall())
cur.execute("""SELECT companyname,mobile,emailid From employer 
where renewalstatus= :param1 and city= :param2 """,{'param1':status,'param2':cit})
print(cur.fetchall())
cur.execute("""SELECT companyname,mobile,emailid From employer
where renewalstatus= :param1 and city= :param2 """,{'param2':cit,'param1':status})
print(cur.fetchall())
con.close()