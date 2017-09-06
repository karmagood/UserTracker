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
        querie = "SELECT * FROM users WHERE username = "+ username
        DB_client.cur.e


    def check_history(self):
        pass

    def update_db(self):
        pass

    def check_threshholds(self):
        pass

    def send_alert(self,fromaddr,toaddrs,message):
        """fromaddr = 'freebsdcommtracker@gmail.com'
        toaddrs  = 'velychko@ucu.edu.ua'
        message = "hello, just testing"""
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