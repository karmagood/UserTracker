class Commands_DB_object:
    def __init__(self,command_id,command,threshold):
        self.command_id = command_id
        self.command = command
        self.threshold = threshold

    def get_command_id(self):
        return self.command_id

    def get_command(self):
        return self.command

    def get_threshold(self):
        return self.threshold