from flask import Flask, render_template
from Cron_job import *
from Shell_client import Shell_client
from DB_client import DB_client
app = Flask(__name__)


shell_client = Shell_client()
db_client = DB_client()
cron = Cron_job()

@app.route('/')
def main_page():
    # all_users
    active_users = cron.get_host_users()
    return render_template("main.html", users=active_users)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    db_user_data = cron.get_db_user_data(username)
    history = cron.check_history()
    return render_template("main.html", name=username)

@app.route('/user/<username>/settings')
def show_user_profile_settings(username):
    # show the user profile for that user
    db_user_data = cron.get_db_user_data(username)
    return 'User %s settings' % username

@app.route('/user/<username>/settings')
def get_last_commands(username):
    return " "

if __name__ == '__main__':
    app.run()