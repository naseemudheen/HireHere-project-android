import flask
import pymysql
from flask import *

app = Flask(__name__)
con = pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='part_time_job')
cmd = con.cursor()
app.secret_key = "qwer";

@app.route('/', methods = ['GET', 'POST'])
def chat():
    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]

    if msg_subject == "register":
        return register(msg_received)
    elif msg_subject == "login":
        return login(msg_received)
    else:
        return "Invalid request."

def register(msg_received):
    firstname = msg_received["firstname"]
    lastname = msg_received["lastname"]
    username = msg_received["username"]
    password = msg_received["password"]

    select_query = "SELECT * FROM users where username = " + "'" + username + "'"
    cmd.execute(select_query)
    records = cmd.fetchall()
    if len(records) != 0:
        return "Another user used the username. Please chose another username."

    insert_query = "INSERT INTO users (first_name, last_name, username, password) VALUES (%s, %s, %s, MD5(%s))"
    insert_values = (firstname, lastname, username, password)
    try:
        cmd.execute(insert_query, insert_values)
        con.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"

def login(msg_received):
    username = msg_received["username"]
    password = msg_received["password"]

    select_query = "SELECT * FROM login where username = '" + username + "' and password = '" + password + "'and type='jobseeker' "
    cmd.execute(select_query)
    records = cmd.fetchall()

    if len(records) == 0:
        return "failure"
    else:
        return "success"

app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)