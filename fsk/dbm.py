import pymysql as p
def connect():
    return p.connect(host="localhost",user="root",password="",database="movie_review",port=3306)


def insert(t):
    con=connect()
    cur=con.cursor()
    sql="insert into details values(%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def check(email):
    con=connect()
    cur=con.cursor()
    sql="select email,password from details where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def userdata():
    con=connect()
    cur=con.cursor()
    sql="select * from details"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def single_user(email):
    con=connect()
    cur= con.cursor()
    sql="select * from details where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data[0]

def updateuser(t):
    con=connect()
    cur=con.cursor()
    sql="update details set name=%s, phone=%s, email=%s, password=%s where email=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
def deleteuser(email):
    con=connect()
    cur=con.cursor()
    sql="delete from details where email=%s"
    cur.execute(sql,email)
    con.commit()
    con.close()
    
def inscom(t):
    con=connect()
    cur=con.cursor()
    sql="insert into doctor values(%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
    
def show():
    con=connect()
    cur=con.cursor()
    sql="select * from doctor"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def insert_grey(t):
    con=connect()
    cur=con.cursor()
    sql="insert into greyman values(%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
    
def show_grey():
    con=connect()
    cur=con.cursor()
    sql="select * from greyman"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def insert_just(t):
    con=connect()
    cur=con.cursor()
    sql="insert into justice values(%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
    
def show_just():
    con=connect()
    cur=con.cursor()
    sql="select * from justice"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def insert_lig(t):
    con=connect()
    cur=con.cursor()
    sql="insert into liger values(%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
    
def show_lig():
    con=connect()
    cur=con.cursor()
    sql="select * from liger"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def insert_vik(t):
    con=connect()
    cur=con.cursor()
    sql="insert into vikram values(%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
    
def show_vik():
    con=connect()
    cur=con.cursor()
    sql="select * from vikram"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def insert_john(t):
    con=connect()
    cur=con.cursor()
    sql="insert into john values(%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()
    
    
def show_john():
    con=connect()
    cur=con.cursor()
    sql="select * from john"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data


