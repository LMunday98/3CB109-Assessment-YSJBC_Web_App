from app.db import connection

def insert(data):
    cursor, conn = connection()
    cursor.execute("insert into " + data[0] + " (" + data[1] + ") values(" + data[2] + ")", (data[3]))
    conn.commit()
    cursor.close()

def user_exist(email):
    cursor, conn = connection()
    cursor.execute("SELECT * from users where user_email=%s", [email])
    
    if cursor.rowcount == 0:
        return False
    else:
        return True
        
def get_user(email):
    cursor, conn = connection()
    cursor.execute("SELECT * from users where user_email=%s", [email])
    results = cursor.fetchone()
    return results