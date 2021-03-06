import sqlite3

con = sqlite3.connect("library.db")
cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS library (name TEXT, author TEXT,book_name TEXT,page INT)")
    con.commit()
def add_data():
    cursor.execute("INSERT INTO library VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def add_input(name,author,book_name,page):
    cursor.execute("INSERT INTO library VALUES(?,?,?,?)",(name,author,book_name,page))
    con.commit()
def get_data():
    cursor.execute("SELECT * FROM library")
    list1 = cursor.fetchall()
    for i in list1:
        print(i)
def get_data2():
    cursor.execute("SELECT name,author FROM library")
    list1 = cursor.fetchall()
    for i in list1:
        print(i)
def get_data3(name):
    cursor.execute("SELECT * FROM library WHERE name = ?",(name,))
    list1 = cursor.fetchall()
    for i in list1:
        print(i)
def update_data(new_page):
    cursor.execute("UPDATE library set page = ? where page = ?",(561,new_page))
    con.commit()
def delete_data(name):
    cursor.execute("Delete  From library where name = ?", (name,))
    con.commit()

#name = input("Name:")
#author = input("Author:")
#book_name = input("Book name:")
#page =  int(input("Page:"))

# add_input(name,author,book_name,page)

#get_data()
#get_data2()
#get_data3("İstanbul Hatırası")

delete_data("Tacettin")
get_data()

con.close()