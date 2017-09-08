#!/usr/bin/python
import MySQLdb

class DB_client:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                                    user="username",         # your username
                                    passwd="pass",  # your password
                                    db="userTracker")        # name of the data base
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
            print( row[0])

        querie = "SELECT * FROM commands"
        self.cur.execute(querie)
        for row in self.cur.fetchall():
            print( row[0])

        querie = "SELECT * FROM user_command"
        self.cur.execute(querie)
        for row in self.cur.fetchall():
            print( row[0])

    def update_users(self,username, history_path):
        """
        updates DB table(users) with new history_path
        :param username: used in select to find needed user
        :param history_path: new history path which will replace old one
        :return: None
        """
        querie = "UPDATE users SET history_path = '{}' WHERE username = {}".format(history_path,
                                                                                 username)
        self.cur.execute(querie)
        self.db.commit()

    def update_commands(self,threshold, command_id):
        """
        updates DB table(commands) with new threshold
        :param threshold: new threshold which woll replace old one
        :param command_id: used in select to track command
        :return: None
        """
        querie = "UPDATE commands SET threshold = {} WHERE command_id = {}".format(threshold,
                                                                                   command_id)
        self.cur.execute(querie)
        self.db.commit()

    def update_user_command(self, counter, user_id, command_id):
        """
        updates DB table(user_command) with new counter
        :param counter: used to replace old value
        :param user_id: used in select to track users command
        :param command_id: used in select to track command
        :return: None
        """
        querie = "UPDATE user_command SET counter = {} WHERE user_id = {} AND command_id = {}".format(counter,
                                                                                                      user_id,
                                                                                                      command_id)
        self.cur.execute(querie)
        self.db.commit()

    def close_db(self):
        self.db.close()