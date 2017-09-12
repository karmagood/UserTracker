import smtplib
import re

def get_host_users(shell_client):
    """
    getting all users on the host and some info about them
    :return: returns list of tuples : [('vlad',tty,logedin@),(...),...]
    """
    command = "last"
    output = shell_client.call(command)
    result = output.split("\n")
    #result = [re.split(re.compile("\s+"), res) for res in result]
    result = [(r[:9].rstrip(" "), r[9:22].rstrip(" "), r[22:39].rstrip(" "), r[39:].rstrip(" "))for r in result[:-3]]
    #print(result)

    return result


def get_db_user_data(username, DB_client):
    """
           :param username Users name
           getting all users data from DB
           :return array of dicts of all users data
           """
    querie = "SELECT * FROM users WHERE username = '{}'".format(username)
    user_data = DB_client.read(querie)
    user_id = user_data[0]["user_id"]
    querie = "SELECT * FROM user_command WHERE user_id = '{}'".format(user_id)
    commands_ids = DB_client.read(querie)
    commands = []
    for item in commands_ids:
        querie = "SELECT * FROM commands WHERE command_id = '{}'".format(item["command_id"])
        rows = DB_client.read(querie)
        for row in rows:
            commands.append(row)
    result_arr = []
    result_arr.append(user_data)
    result_arr.append(commands_ids)
    result_arr.append(commands)
    return result_arr


def check_thresholds(username, command, DB_client):
    """
           :param username: users username, used to get additional data on user from DB
           :param command: comand to check for ('ls')
           if commands threshold is reached by user, send_alert method
           will be used to notify user.
           """
    querie = "SELECT * FROM users WHERE username = '{}'".format(username)
    user_data = DB_client.read(querie)
    querie = "SELECT * FROM commands WHERE command = '{}'".format(command)
    command_dict = DB_client.read(querie)
    querie = "SELECT * FROM user_command WHERE user_id = '{}' AND command_id = '{}'".format(user_data[0]["user_id"],
                                                                                            command_dict[0][
                                                                                                "command_id"])
    user_command = DB_client.read(querie)
    if command_dict[0]["threshold"] <= user_command[0]["counter"]:
        msg = "You({}) have reached the limit on using {} command: {}/{}.".format(username,
                                                                                  command,
                                                                                  user_command[0]["counter"],
                                                                                  command_dict[0]["threshold"])
        send_alert(user_data[0]["email"],msg)
        #"You have reached the limit on using " + command + " command")


def send_alert(toaddrs,message):
        """
        Sending email param: message
        to address param:toaddrs
        """
        fromaddr = 'freebsdcommtracker@gmail.com'
        msg = """From: {}
To: {},
Subject: FreeBSD security controll

{}

Contact admin to increase commands threshold or to erase your previous logs.
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




def check_history(shell_client, username):
        shell_client.call("history")

def update_db(user_id, command_id, username, history_path, threshold, counter, DB_client):
    """
    fills usertracker Db user table with new users data
    :param user_id:
    :param command_id:
    :param username:
    :param history_path:
    :param threshold:
    :param counter:
    """
    DB_client.update_users(username, history_path)
    DB_client.update_commands(command_id, threshold)
    DB_client.update_user_command(counter,user_id, command_id)

if __name__ == '__main__':
    import Shell_client
    get_host_users(Shell_client.Shell_client())