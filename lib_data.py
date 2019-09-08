import sqlite3
x=25698
def connect():
    conn=sqlite3.connect('libarary.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS LIB(BOOK TEXT NOT NULL, AUTHOR TEXT,
                                    YEAR INT , ISBN INT PRIMARY KEY NOT NULL)''')
    conn.commit()
    conn.close()
    
def insert1(a,b,c,d):
    print(a,b,c,d)
    conn=sqlite3.connect('libarary.db')
    conn.execute(f"INSERT INTO LIB VALUES('{a}','{b}',{c},{d})")
    conn.commit()
    conn.close()
    
def view():
    cursor=conn.execute('SELECT * FROM LIB')
    conn.close()
    return cursor

def update(x):
    conn=sqlite3.connect('librarary.db')
    conn.execute("UPDATE LIB SET BOOK=(?),AUTHOR=(?),YEAR=(?) WHERE ISBN=?",(x[0],x[1],x[2],x[3]))
    conn.commit()
    conn.close()
                
def delete1(x):
    conn=sqlite3.connect('librarary.db')
    conn.execute(f"DELETE FROM LIB WHERE ISBN={x}")
    conn.commit()
    conn.close()
def select(x):
    conn=sqlite3.connect('librarary.db')
    cursor=conn.execute(f"SELECT * FROM LIB WHERE ISBN={x}")
    conn.close()
    return cursor
connect()
