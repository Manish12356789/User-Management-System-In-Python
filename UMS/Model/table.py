from Model.database import Database


class Table(Database):
    def __init__(self):
        db = Database()
        conn = db.connection()
        self.cur = conn.cursor()

    def create_table(self):
        # drop table if already exists
        self.cur.execute("DROP TABLE IF EXISTS ums_admin")
        self.cur.execute("DROP TABLE IF EXISTS ums_user")

        # create ums_admin table
        self.cur.execute("CREATE TABLE ums_admin (admin_id INT(11) AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), address VARCHAR(255), phone_num BIGINT(20) )")

        # create ums_user table
        self.cur.execute("CREATE TABLE ums_user (user_id INT(11) AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), address VARCHAR(255), phone_num BIGINT(20) )")
