import sqlite3
connect = sqlite3.connect("SATSQL.sql")
cursor = connect.cursor()
def data_entry(WORD,Definition) : 
    connect.execute('INSERT INTO VC VALUES(?, ?)',(WORD,Definition))
    connect.commit()
def get_data() :
    cursor.execute('SELECT * FROM VC')
    data= cursor.fetchall()
    for i in data :
        print(i)