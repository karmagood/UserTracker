import smtplib

def get_host_users(shell_client):
    """
    getting all users on the host and some info about them
    :return: returns list of dictionaries : [{"Vlad":[tty,logedin@]},{...},...]
    """
    command = "who"
    output = shell_client.call(command)
    result = output.strip().split(" ")
    result = filter(None, result)
    j = 0
    name_arr = []
    for i in range(len(result) / 5):
        u_data = []
        for y in range(j + 1, j + 5):
            u_data.append(result[y])
        name_arr.append({result[j]: u_data})
        j += 5
    return name_arr


def get_db_user_data(username, DB_client):
        """
        :param username Users name
        getting all users data from DB

        :return array of dicts of all users data
        """
        querie = "SELECT * FROM users WHERE username = "+ username
        user_data = DB_client.read(querie)
        user_id = user_data[0]["user_id"]
        querie = "SELECT * FROM user_command WHERE user_id = "+ str(user_id)
        commands_ids = DB_client.read(querie)
        commands = []
        for item in commands_ids:
            querie = "SELECT * FROM commands WHERE command_id = "+ str(item["command_id"])
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
        :param username: users username to cheak for ('aba')
        :param command: comand to check for ('ls')


        if commands threshold is reached by user, email will be sent
        to user notifying him.
        """
        querie = "SELECT * FROM users WHERE username = "+ username
        user_data = DB_client.read(querie)
        querie = "SELECT * FROM commands WHERE command = "+ command
        command_dict =  DB_client.read(querie)
        querie = "SELECT * FROM user_command WHERE user_id = "+str(user_data["user_id"]) + "AND command_id = " + str(command_dict["command_id"])
        user_command = DB_client.read(querie)
        if command_dict["threshold"] <= user_command["count"]:
            send_alert(user_data["email"],"You have reached the limit on using "+ command_dict["command"] + " command")

def send_alert(toaddrs,message):
        """
        Sending email param: message
        to address param:toaddrs
        """
        fromaddr = 'freebsdcommtracker@gmail.com'
        msg = """From: {}
To: {},
Subject: Just a message

{}
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




def check_history(db_user_data):
        pass

def update_db(db_user_data):
        pass
