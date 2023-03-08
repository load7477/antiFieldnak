import pymysql

table = 'fc'

def getuserinfo(ids):
    if isregister(ids):
        con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db=table, charset='utf8')
        cur = con.cursor(pymysql.cursors.DictCursor)
        cur.execute(f"SELECT * FROM account WHERE ids='"+str(ids)+"';")
        return cur.fetchone()
    else:
        createAccount(ids)

def isregister(name):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db=table, charset='utf8')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM account WHERE ids='"+str(name)+"';")
    result = cur.fetchone()
    if result == None:
        return False
    else:
        return True

def createAccount(discord):
    con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db=table, charset='utf8')
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO account(ids, count) VALUES('{discord}', '1');")
    con.commit()  
    return "ok"

def addcount(userinfo, name):
    if isregister(name):
        con = pymysql.connect(user='root', passwd='', host='127.0.0.1', db=table, charset='utf8')
        cur = con.cursor() 
        cur.execute(f"UPDATE account SET count={userinfo['count']+1} WHERE ids='{userinfo['ids']}';") 
        con.commit()
        return True
    else:
        createAccount(name)