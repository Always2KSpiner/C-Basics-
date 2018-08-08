'''
Created on 28-Jun-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
cur.execute("""Create Table user1(
            userid number(10) primary key,
            username varchar2(30) not null,
            password varchar2(20) not null,
            usertype varchar2(20) CHECK (usertype IN ('Employer','Jobseeker'))
            )""")
cur.execute("""insert into user1 values(1,'jobs@infosys.com','jobs@infosys','Employer')""")
uid1=2
uname1='careers@accenture.com'
upwd1='Acc1'
utype1='Employer'
cur.execute("""insert into user1 values(:A,:B,:C,:D)""",(uid1,uname1,upwd1,utype1))
uid2=3
uname2='rahulitsme@gmail.com'
upwd2='rahulindia93'
utype2='Jobseeker'
cur.execute("""insert into user1 values(:par1,:par2,:par3,:par4)\n""",{'par1':uid2,'par2':uname2,'par3':upwd2,'par4':utype2})
uid3=int(input("ENTER USER ID\n"))
uname3=input("ENTER USER NAME\n")
upwd3=input("ENTER USER PASSWORD\n")
utype3=input("ENTER USER TYPE\n")   
cur.execute("""insert into user1 values(:var1,:var2,:var3,:var4)""",{'var1':uid3,'var2':uname3,'var3':upwd3,'var4':utype3})       
cur.execute("SELECT * From user1")
data=cur.fetchall()
for line in data:
    print(line)
con.commit()
con.close()