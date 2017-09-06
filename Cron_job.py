from Shell_client import *

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
            name_arr.append(result[j])
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

    def send_alert(self):
        pass