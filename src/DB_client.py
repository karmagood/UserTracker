#!/usr/bin/python
import MySQLdb

class DB_client:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                                    user="root",         # your username
                                    passwd="@Kennym007",  # your password
                                    db="usertracker")        # name of the data base
        self.cur = self.db.cursor(MySQLdb.cursors.DictCursor)       #cursor that lets execute quiery

    def read(self,querie):
        # Accepts read querie and executes it
        self.cur.execute(querie)
        result = self.cur.fetchall()
        return result

    def write(self,querie):
        # Accepts write querie and executes it
        self.cur.execute(querie)
        self.db.commit()

    def show_all(self):
        """
        displays all DB tables content
        :return: None
        """
        querie = "SELECT * FROM users"
        self.cur.execute(querie)
        for row in self.cur.fetchall():
            print(row)

        querie = "SELECT * FROM commands"
        self.cur.execute(querie)
        for row in self.cur.fetchall():
            print(row)

        querie = "SELECT * FROM user_command"
        self.cur.execute(querie)
        for row in self.cur.fetchall():
            print(row)

    def close_db(self):
        self.db.close()