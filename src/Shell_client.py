import subprocess

class Shell_client:
    def __init__(self):
        pass

    def call(self,command):
        comm_array = command.split(" ")
        proc = subprocess.Popen(comm_array, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        return output

