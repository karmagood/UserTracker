class User_command_DB_object:
    def __init__(self,user_id,command_id,count):
        self.user_id = user_id
        self.command_id = command_id
        self.count = count

    def get_user_id(self):
        return self.user_id

    def get_command_id(self):
        return self.command_id

    def get_count(self):
        return self.count
