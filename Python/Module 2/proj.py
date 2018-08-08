'''
Created on 08-Jul-2018

@author: anitr
'''
import cx_Oracle
con=cx_Oracle.connect('ani/mycycle.com')
cur=con.cursor()
def maxlike():
    cur.execute("""select c.picid,likes,userid from (select picid,count(picid) as likes from instalike
    group by picid order by count(picid)desc)c,instapic d where rownum=1 and c.picid=d.picid and userid=:var""",(user_id,))
    data=cur.fetchall()
    for line in data:
        print("MOST LIKED PIC")
        print("PICID:",line[0],"\nLIKES:",line[1],"\nUSERID:",line[2])
def minlike():
    cur.execute("""select c.picid,likes,userid from (select picid,count(picid) as likes from instalike 
    group by picid order by count(picid))c,instapic d where rownum=1 and c.picid=d.picid and userid=:var""",(user_id,))
    data=cur.fetchall()
    for line in data:
        print("MINLIKED PIC")
        print("PICID:",line[0],"\nLIKES:",line[1],"\nUSERID:",line[2])
def uselike():        
    cur.execute("""select c.userid,likes from (select userid,count(userid) as likes from instalike
     group by userid order by count(userid)desc) c,instapic d where rownum=1 and c.userid=d.userid""")
    data=cur.fetchall()
    for line in data:
        print("USER WHO LIKED MOST PIC")
        print("USERID",line[0],"\nLIKES:",line[1])
def tag():
    cur.execute("""select * from instapic where tag='Music'""")
    data=cur.fetchall()
    print("PICS RELATED TO MUSIC")
    for line in data:
        print("PICID:",line[0],"CAPTION:",line[1],"DATE:",line[2],"USERID:",line[3])  
def poptag():
    cur.execute("""select * from (select tag,count(tag) as Popular from instapic group by tag order by count(tag)desc)
     where rownum=1""")
    data=cur.fetchall()
    for line in data:
        print("MOST POPULAR TAG")
        print("TAG:",line[0],"\nUSE COUNT:",line[1]) 
def liked_user():
    cur.execute("""select c.userid,sum(likes) from (select userid,count(userid) as likes from instalike group by userid
    order by count(userid)desc) where rownum=2""")
    data=cur.fetchall()
    for line in data:
        print("MOST LIKED USER")
        print("USERID",line[0],"\nLIKES:",line[1])
def tagold():
    cur.execute("""update instapic  set tagold='Old' where  post < sysdate - interval '3' year""")
    cur.execute("""SELECT * from instapic""")
    print("UPDATED TABLE")
    data=cur.fetchall()
    for line in data:
        print(line)
def delold():
    cur.execute("""delete from instapic a inner join instauser b where a.userid=b.userid  and post<sysdate - interval '1' year""")
    cur.execute("""SELECT * from instauser""")
    print("UPDATED TABLE")
    data=cur.fetchall()
    for line in data:
        print(line)
user_id=int(input("ENTER USERID\n"))
cho=1
while cho!=0:
    print("""\n____MENU___\n1.Max Likes \n2.Min Likes \n3.Who liked most\n4.Music pictures\n5.Popular Tag\n6.Most liked User
7.Old Tagging\n8.Delete Inactive Users\n0.Exit""")
    cho=int(input("ENTER CHOICE\n"))
    if cho==1:
        maxlike()
    elif cho==2:
        minlike()
    elif cho==3:
        uselike()
    elif cho==4:
        tag()
    elif cho==5:
        poptag()
    elif cho==6:
        liked_user()
    elif cho==7:
        tagold()
    elif cho==8:
        delold()
    else:
        print("EXIT\n")  
con.commit() 
con.close()