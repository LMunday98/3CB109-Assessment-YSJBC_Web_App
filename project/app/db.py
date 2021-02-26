import MySQLdb

def connection():
    conn = MySQLdb.connect(
        host="127.0.0.1",
        user = "root",
        passwd = "",
        db = "flask")
    c = conn.cursor()

    return c, conn

def insert(data):
    cursor, conn = connection()
    cursor.execute("insert into " + data[0] + " (" + data[1] + ") values(" + data[2] + ")", (data[3]))
    conn.commit()
    cursor.close()