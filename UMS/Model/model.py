from mysql.connector import Error
from Model.database import Database


class Model:
    def __init__(self):
        self.error = Error()
        db = Database()
        self.conn = db.connection()

    def admin_validate(self, em, pw):
        cur = self.conn.cursor()

        try:
            sql = "SELECT admin_id, email, password FROM ums_admin WHERE email = %s AND password = %s"
            cur.execute(sql, (em, pw,))
            row = cur.fetchone()
            aid = row[0]
            email = row[1]
            password = row[2]
            #print(aid, email, password)
            return aid, email, password
        except:
            return "Incorrect email and password"

    def user_validate(self, em, pw):
        cur = self.conn.cursor()

        try:
            sql = "SELECT user_id, email, password FROM ums_user WHERE email = %s AND password = %s"
            cur.execute(sql, (em, pw,))
            row = cur.fetchone()
            uid = row[0]
            email = row[1]
            password = row[2]
            # print(email, password)
            return uid, email, password
        except:
            return "Sorry!", "Your Email and password is Wrong."

    def add_to_user_db(self, user_data):         # To add list data into the mysql database for normal user
        cur = self.conn.cursor()

        #print(user_data)
        ins_ur_sql = "INSERT INTO ums_user (user_name, email, password, address, phone_num) VALUES(%s, %s, %s, %s, %s)"
        ins_ur_val = (user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
        cur.execute(ins_ur_sql, ins_ur_val)
        self.conn.commit()
        return "Your Sign UP is Finished."

    def user_data_show(self, uid):
        cur = self.conn.cursor()
        sql = "SELECT * FROM ums_user WHERE user_id = %s"
        cur.execute(sql, (uid,))
        data = cur.fetchone()
        #print(data)
        return data

    def admin_data_show(self, aid):
        cur = self.conn.cursor()
        sql = "SELECT * FROM ums_admin WHERE admin_id = %s"
        cur.execute(sql, (aid,))
        data = cur.fetchone()
        return data

    def all_user_data_for_admin(self):
        cur = self.conn.cursor()
        sql = "SELECT * FROM ums_user"
        cur.execute(sql)
        rows = cur.fetchall()
        #print(rows)
        return rows

    def update_user(self, edit_data, uid):
        cur = self.conn.cursor()
        sql = "UPDATE ums_user SET user_name = %s, email = %s, password = %s, address = %s, phone_num = %s WHERE user_id = %s"
        data = (edit_data[0], edit_data[1], edit_data[2], edit_data[3], edit_data[4], uid)
        cur.execute(sql, data)
        self.conn.commit()
        return "Updated Successfully."

    def update_admin(self, data, aid):
        cur = self.conn.cursor()
        sql = "UPDATE ums_admin SET user_name = %s, email = %s, password = %s, address = %s, phone_num = %s WHERE admin_id = %s"
        data = (data[0], data[1], data[2], data[3], data[4], aid)
        cur.execute(sql, data)
        self.conn.commit()
        return "Updated Successfully."

    def delete_user_by_admin(self, un):
        cur = self.conn.cursor()
        #print(uid)
        sql = "DELETE FROM ums_user WHERE user_name = %s"
        cur.execute(sql, (un,))
        self.conn.commit()
        return "Deleted Successfully!"

