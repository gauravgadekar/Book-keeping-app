import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, author TEXT,year INTEGER,ISBN INTEGER)")
        self.conn.commit()


    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book values (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view(sglobal selected_tupleelf):
            self.cur.execute("SELECT * from book")
            row=self.cur.fetchall()
            return row

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        row=self.cur.fetchall()
        self.conn.commit()
        return row

    def delete(self,id):
            self.cur.execute("DELETE FROM book where id=?",(id,))
            self.conn.commit()

    def update(self,id,title,author,year,isbn):
            self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE ID=?",(title,author,year,isbn,id))
            self.conn.commit()

    def __del__(self):
        self.conn.close()
