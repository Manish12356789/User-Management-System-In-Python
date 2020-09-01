class Database:
    def __init__(self):
        pass

    def connection(self):
        import mysql.connector as mc  # import mysql database connector

        # database connection
        conn = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="ums"
        )
        #cur = conn.cursor()
        #em = "samrat@gmail.com"
        #pw = "samrat"
        #sql = "SELECT admin_id, email, password FROM ums_admin WHERE email = %s AND password = %s"
        #cur.execute(sql, (em, pw,))
        #rows = cur.fetchone()
        #e = rows[1]
        #p = rows[2]
        #print(e, p)

        # check the database is connected or not, using is_connected() function
        if conn.is_connected():
            print("Database connected successfully!")

        return conn


#db = Database()
#db.connection()
