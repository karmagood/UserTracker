from Shell_client import *

class Cron_job:
    def __init__(self):
        self.shell_c = Shell_client()

    def get_host_users(self):
        command = "who -a"
        result = self.shell_c.call(command)
        return result

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