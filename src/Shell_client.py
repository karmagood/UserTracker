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
        output = subprocess.check_output(command, executable="bash", shell=True )
        return output
