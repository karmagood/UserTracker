class Users_DB_object:
    def __init__(self,user_id,username,email,history_path):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.history_path = history_path

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_history_path(self):
        return self.history_path