from Shell_client import *
import smtplib
from DB_client import *

class Cron_job:
    def __init__(self):
        self.shell_c = Shell_client()
        self.DB_client = DB_client()

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
        user_id = user_data[0][0]
        querie = "SELECT * FROM user_command WHERE user_id = "+ str(user_id)
        commands_ids = self.DB_client.read(querie)
        commands = []
        for item in commands_ids:
            querie = "SELECT * FROM commands WHERE command_id = "+ str(item[2])
            rows = self.DB_client.read(querie)
            for row in rows:
                commands.append(row)





    def check_history(self):
        pass

    def update_db(self):
        pass

    def check_threshholds(self):
        pass

    def send_alert(self,toaddrs,message):
        """Sending pram: message to param:toaddrs"""
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