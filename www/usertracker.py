from flask import Flask, render_template
from src import utils
from src.Shell_client import Shell_client
#from src.DB_client import DB_client
app = Flask(__name__)


shell_client = Shell_client()
#db_client = DB_client()


@app.route('/')
def main_page():
    active_users = get_host_users(shell_client)
    return render_template("main.html", users=active_users)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    #db_user_data = get_db_user_data(username,db_client)
    history = check_history(shell_client, username)
    print(history)
    return render_template("main.html", name=username, history=history)

@app.route('/user/<username>/settings')
def show_user_profile_settings(username):
    # show the user profile for that user
    db_user_data = get_db_user_data(username,db_client)
    return 'User %s settings' % username

@app.route('/user/<username>/last_commands')
def get_last_commands(username):
    return " "

if __name__ == '__main__':
    app.run()
