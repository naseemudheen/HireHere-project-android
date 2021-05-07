import pymysql
from flask import *



app = Flask(__name__)
con = pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='part_time_job')
cmd = con.cursor()
app.secret_key = "qwer";



@app.route('/login', methods=['post', 'get'])
def login():
    username = request.form["username"]
    password = request.form["password"]


    cmd.execute("SELECT `login`.*,`jobseeker`.`firstname`,`jobseeker`.`lastname` FROM  `login` JOIN `jobseeker` ON `login`.`id`=`jobseeker`.`login_id` WHERE `username`='"+username+"' AND `password`='"+password+"'")
    res = cmd.fetchone()
    if res == None:
        result = {'status':'failure'}
        return jsonify(result)
    else:
        if res[3] == 'jobseeker':
            result = {'status': 'success','username':res[2],'uid':res[0],'fullname':res[4]+'  '+res[5]}
            return jsonify(result)
        else:
            result = {'status': 'failure'}
            return jsonify(result)

@app.route('/register', methods=['post', 'get'])
def register():
    firstname = request.get_json()["firstname"]
    lastname = request.get_json()["lastname"]
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    email = request.get_json()["email"]
    place = request.get_json()["place"]
    post = request.get_json()["post"]
    pin = request.get_json()["pin"]
    phone = request.get_json()["phone"]
    select_qry = "SELECT * from login where username = '"+username+"'"
    cmd.execute(select_qry)

    records = cmd.fetchall()
    if len(records) != 0:
        return "username"

    try:
        cmd.execute("INSERT INTO login(username,password,type) values ('"+username+"','"+password+"','jobseeker');")
        id = con.insert_id()
        insert_qry2 = "INSERT INTO jobseeker (firstname, lastname, place, post,pin,email,phoneno,login_id) VALUES ('" + firstname + "','" + lastname + "','" + place + "','" + post + "','" + str(pin) + "','" + email + "','" + str(phone) + "','"+str(id)+"')"
        cmd.execute(insert_qry2)
        con.commit()
        return "success"
    except Exception as e:
        return "failure"


@app.route('/viewjob', methods=['post', 'get'])
def viewjob():
    cmd.execute("SELECT `job`.*,`employer`.`company` FROM `job` JOIN `employer` ON `job`.`company_id`=`employer`.`id`")
    res = cmd.fetchall()
    jobs = []

    for result in res:
        contents  ={'id':result[0],'job':result[1],'salary':result[3],'place':result[4],'contact':result[5],'company':result[6]}
        jobs.append(contents)
    return jsonify(jobs)

@app.route('/jobApply', methods=['post', 'get'])
def jobApply():
    uid=request.form['user_id']
    job_id=request.form['job_id']
    try:
        cmd.execute("SELECT * FROM `job-applied` WHERE `login_id`='"+uid+"' AND `job_id` ='"+job_id+"'")
        res = cmd.fetchone()
        if res is None:
            cmd.execute("INSERT INTO `job-applied` (`login_id`,`job_id`) VALUES ('"+uid+"','"+job_id+"')")
            con.commit()
            return "success"
        else:
            return "failure"
    except Exception as e:
        return "failure"


@app.route('/viewAppliedjob', methods=['post', 'get'])
def viewAppliedjob():
    uid=request.form['login_id']
    cmd.execute("SELECT `job`.`job`,`employer`.`company` FROM `job` JOIN `employer` ON `job`.`company_id`=`employer`.`id` WHERE `job`.`id` IN(SELECT `job_id` FROM `job-applied` WHERE `login_id`='"+uid+"')")
    res = cmd.fetchall()
    appliedjobs = []

    for result in res:
        contents  = {'job':result[0],'company':result[1]}
        appliedjobs.append(contents)

    return jsonify(appliedjobs)


@app.route('/sendComplaint', methods=['post', 'get'])
def sendComplaint():
    uid = request.form["uid"]
    cmpmsg = request.form["msg"]

    today = date.today()

    cmd.execute("INSERT INTO `complaint`(`complaint`,`date`,`login_id`)VALUES('"+cmpmsg+"','"+str(today)+"','"+str(uid)+"')")
    con.commit()
    return "success"

@app.route('/sendFeedback', methods=['post', 'get'])
def sendFeedback():
    uid = request.form["uid"]
    cmpmsg = request.form["msg"]

    today = date.today()

    cmd.execute("INSERT INTO `feedback`(`feedback`,`date`,`login_id`)VALUES('"+cmpmsg+"','"+str(today)+"','"+str(uid)+"')")
    con.commit()
    return "success"





app.run(host="0.0.0.0" ,port=5000,threaded=True ,debug=True)
