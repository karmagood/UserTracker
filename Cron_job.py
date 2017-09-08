from Shell_client import *
import smtplib
from DB_client import *


class Cron_job:
    def __init__(self):
        self.shell_c = Shell_client()
        self.DB_client = DB_client()


    def get_host_users(self):
        """
        getting all users on the host and some info about them
        :return: returns list of dictionaries : [{"Vlad":[tty,logedin@]},{...},...]
        """
        command = "who"
        output = self.shell_c.call(command)
        result = output.strip().split(" ")
        result = filter(None,result)
        j = 0
        name_arr = []
        for i in range(len(result)/5):
            u_data = []
            for y in range(j+1,j+5):
                u_data.append(result[y])
            name_arr.append({result[j]:u_data})
            j += 5
        return name_arr

    def get_db_user_data(self,username):
        """
        :param username Users name
        getting all users data from DB

        :return array of dicts of all users data
        """
        querie = "SELECT * FROM users WHERE username = '{}'".format(username)
        user_data = self.DB_client.read(querie)
        user_id = user_data[0]["user_id"]
        querie = "SELECT * FROM user_command WHERE user_id = '{}'".format(user_id)
        commands_ids = self.DB_client.read(querie)
        commands = []
        for item in commands_ids:
            querie = "SELECT * FROM commands WHERE command_id = '{}'".format(item["command_id"])
            rows = self.DB_client.read(querie)
            for row in rows:
                commands.append(row)
        result_arr = []
        result_arr.append(user_data)
        result_arr.append(commands_ids)
        result_arr.append(commands)
        return result_arr




    def check_history(self):
        pass

    def update_db(self):

        pass

    def check_thresholds(self, username, command):
        """
        :param username: users username, used to get additional data on user from DB
        :param command: comand to check for ('ls')


        if commands threshold is reached by user, send_alert method
        will be used to notify user.
        """
        querie = "SELECT * FROM users WHERE username = '{}'".format(username)
        user_data = self.DB_client.read(querie)
        querie = "SELECT * FROM commands WHERE command = '{}'".format(command)
        command_dict =  self.DB_client.read(querie)
        querie = "SELECT * FROM user_command WHERE user_id = '{}' AND command_id = '{}'".format(user_data[0]["user_id"],
                                                                                                command_dict[0]["command_id"])
        user_command = self.DB_client.read(querie)
        if command_dict[0]["threshold"] <= user_command[0]["counter"]:
            self.send_alert(user_data[0]["email"],
                            "You have reached the limit on using "+ command + " command")


    def send_alert(self,toaddrs,message):
        """
        Sending email param: message
        to address param:toaddrs
        """
        fromaddr = 'freebsdcommtracker@gmail.com'
        msg = """From: {}
To: {},
Subject: Alert!

{}
"""
        username = 'freebsdcommtracker@gmail.com'
        password = 'Freebsd2017'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        msg = msg.format(fromaddr,toaddrs,message)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()