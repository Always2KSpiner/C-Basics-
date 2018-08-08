'''
Created on 29-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
cur.execute("""Create Table account(
            customerid number(10) primary key,
            accountno varchar2(15) not null,
            accounttype varchar2(15) CHECK (accounttype IN ('Savings','Current','Recurring')),
            balance number(10) not null
            )""")
cid=101
acno='IBI100'
cur.executemany("""insert into account values(:par1,:par2,:par3,:par4)""",
                [{'par1':cid,'par2':acno+'1','par3':'Savings','par4':0},
                 {'par1':cid+1,'par2':acno+'2','par3':'Current','par4':1200},
                 {'par1':cid+2,'par2':acno+'3','par3':'Savings','par4':6543},
                 {'par1':cid+3,'par2':acno+'4','par3':'Recurring','par4':7500},
                 {'par1':cid+4,'par2':acno+'5','par3':'Current','par4':0}
                 ])
print("ORIGINAL TABLE")
cur.execute("SELECT * from account")
data=cur.fetchall()
for line in data:
    print(line)
print("\nCUSTOMER WITH MAX BALANCE")
cur.execute("select customerid,balance from account where balance=(select max(balance) from account)")
data=cur.fetchall()
for line in data:
    print(line) 
print("\nBALANCE OF ID 102")
cur.execute("select balance from account where customerid=102")  
data=cur.fetchall()
for acct_bal in data:
    print(acct_bal)
    acct_bal=acct_bal[0]+2000
cur.execute("update account set balance=:var where customerid=102",(acct_bal,))
print("\nUPDATED BALANCE")
cur.execute("select balance from account where customerid=102") 
data=cur.fetchall()
for line in data:
    print(line[0])
cur.execute("DELETE FROM account where balance=0 and accounttype='Current'")
print("\nUPDATED TABLE")
cur.execute("SELECT * from account")
data=cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()