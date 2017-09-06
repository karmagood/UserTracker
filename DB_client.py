#!/usr/bin/python
import MySQLdb

class DB_client:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                                    user="username",         # your username
                                    passwd="pass",  # your password
                                    db="userTracker")        # name of the data base
        self.cur = self.db.cursor()       #cursor that lets execute quiery

    def read(self,querie):
        # Accepts read querie and executes it
        self.cur.execute(querie)
        result = self.cur.fetchall()
        return result

    def write(self,querie):
        # Accepts write querie and executes it
        self.cur.execute(querie)



    def show_all(self):
        for row in self.cur.fetchall():
            print( row[0])


    def close_db(self):
        self.db.close()