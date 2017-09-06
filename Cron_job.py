from Shell_client import *
import smtplib


class Cron_job:
    def __init__(self):
        self.shell_c = Shell_client()

    def get_host_users(self):
        command = "who"
        output = self.shell_c.call(command)
        result = output.strip().split(" ")
        result = filter(None,result)
        j = 0
        name_arr = []
        for i in range(5/len(result)):
            u_data = []
            for y in range(j+1,j+5):
                u_data.append(result[y])
            name_arr.append({result[j]:u_data})
            j += 5
        return name_arr

    def get_db_user_data(self):
        pass

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