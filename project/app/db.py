import MySQLdb

def connection():
    conn = MySQLdb.connect(
        host="127.0.0.1",
        user = "root",
        passwd = "",
        db = "flask")
    c = conn.cursor()

    return c, conn