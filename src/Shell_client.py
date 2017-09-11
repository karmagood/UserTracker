import subprocess

class Shell_client:
    def __init__(self):
        pass

    def call(self,command):
        """
        executes given command.
        :param command: command that will be executed.
        :return: output of command execution.
        """
        comm_array = command.split(" ")
        proc = subprocess.Popen(comm_array, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        return output
