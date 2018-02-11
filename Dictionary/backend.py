import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    
    if (title == ""):
        s_t = 0
    else:
        s_t = 1
    if (author == ""):
        s_a = 0
    else:
        s_a = 1
    if (year == ""):
        s_y = 0
    else:
        s_y = 1
    if (isbn == ""):
        s_i = 0
    else:
        s_i = 1
    
    if (s_t+s_a+s_y+s_i == 0):
        return((0,"No Keywords","",0,0))
    elif(title == ""):
        return((0,"title keyword needed","",0,0))
    else:
        cur.execute("SELECT * FROM book WHERE title LIKE \"%" +s_t*str(title)+ s_t*"%\" " 
                    + s_a*"AND author LIKE \"%" +s_a*str(author)+ s_a*"%\" " 
                    + s_y*" AND year LIKE \"%" +s_y*str(year)+ s_y*"%\" " 
                    + s_i*" AND isbn LIKE \"%" +s_i*str(isbn)+ s_i*"%\" " 
                    )
    rows=cur.fetchall()
    conn.close()
    return (rows)

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
