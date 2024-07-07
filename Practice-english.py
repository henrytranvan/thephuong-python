import sqlite3
connect = sqlite3.connect("SATSQL.sql")
cursor = connect.cursor()
def data_entry(WORD,Definition) : 
    connect.execute('INSERT INTO VC VALUES(?, ?)',(WORD,Definition))
    connect.commit()
def get_data() :
    cursor.execute('SELECT * FROM VC')
    data= cursor.fetchall()
    count = int(input("Bạn đã học được bao nhiêu từ vựng tiếng anh ? "))
    while count == count+11  :
        A = data[count]
        print(A)
        count=count+1
get_data()
cursor.close()
connect.close()