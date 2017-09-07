from Shell_client import *
import smtplib
from DB_client import *
from Users_DB_object import *
from User_command_DB_object import *
from Commands_DB_object import *


class Cron_job:
    def __init__(self):
        self.shell_c = Shell_client()
        self.DB_client = DB_client()
        self.Users_DB_object = Users_DB_object()
        self.U

    def get_host_users(self):
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

        collects data from user

        """
        querie = "SELECT * FROM users WHERE username = "+ username
        user_data = self.DB_client.read(querie)
        user_id = user_data[0]["user_id"]
        querie = "SELECT * FROM user_command WHERE user_id = "+ str(user_id)
        commands_ids = self.DB_client.read(querie)
        commands = []
        for item in commands_ids:
            querie = "SELECT * FROM commands WHERE command_id = "+ str(item["command_id"])
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
        :param username: users username to cheak for ('aba')
        :param command: comand to check for ('ls')


        if commands threshold is reached by user, email will be sent
        to user notifying him.
        """
        querie = "SELECT * FROM users WHERE username = "+ username
        user_data = self.DB_client.read(querie)
        querie = "SELECT * FROM commands WHERE command = "+ command
        command_dict =  self.DB_client.read(querie)
        querie = "SELECT * FROM user_command WHERE user_id = "+str(user_data["user_id"]) + "AND command_id = " + str(command_dict["command_id"])
        user_command = self.DB_client.read(querie)
        if command_dict["threshold"] <= user_command["count"]:
            self.send_alert(user_data["email"],"You have reached the limit on using "+ command_dict["command"] + " command")


    def send_alert(self,toaddrs,message):
        """
        Sending email param: message
        to address param:toaddrs
        """
        fromaddr = 'freebsdcommtracker@gmail.com'
        msg = """From: {}
To: {},
Subject: Just a message

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