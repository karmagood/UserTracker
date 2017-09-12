from Shell_client import *
from DB_client import *
from utils import *


class CronJob:
    def __init__(self, shell_client=None, db_client=None):
        self.shell_client = Shell_client()
        self.DB_client = DB_client()

    def run_job(self):
        # all_users = todo
        active_users = get_host_users(self.shell_client)
        for user in active_users:
            db_user_data = get_db_user_data(username=user, DB_client=self.DB_client)
            checked_user_data = check_history(db_user_data)
            update_db(checked_user_data)
            for command in checked_user_data["commands"]:
                check_thresholds(user, command, self.DB_client)