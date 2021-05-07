import pymysql
from flask import *
from datetime import date

app = Flask(__name__)
con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='part_time_job')
cmd = con.cursor()
app.secret_key = "qwer";


@app.route('/', methods=['get'])
def main():
    return render_template('login.html')


@app.route('/login', methods=['post', 'get'])
def login():
    uname = request.form['textfield']
    passwd = request.form['textfield2']
    cmd.execute("select * from `login` where `username`='" + uname + "' and `password` ='" + passwd + "'")
    res = cmd.fetchone()
    if res is None:
        return "<script> alert('invalid username or password')</script>"
    else:
        if res[3] == 'admin':
            return '''<script>window.location='/admin_home' </script>'''
        elif res[3] == 'employer':
            session['lid'] = res[0]
            return '''<script>window.location='/employer_home' </script>'''
        else:
            return "<script> alert('invalid username or password')</script>"


@app.route('/admin_home')
def admin_home():
    return render_template('Admin/admin.html')


@app.route('/manage_job_seeker')
def manage_job_seeker():
    cmd.execute("SELECT `jobseeker`.*,`login`.* FROM `login` JOIN `jobseeker` ON `jobseeker`.`login_id`=`login`.`id`")
    result = cmd.fetchall()

    return render_template('Admin/manage_job_seeker.html', val=result)


@app.route('/block_jobseeker', methods=['get', 'post'])
def block_jobseeker():
    id = request.args.get('id')
    cmd.execute("update login set login.type='blocked' where id='" + str(id) + "'")
    con.commit()
    return '''<script>alert('Jobseeker Blocked');window.location='/manage_job_seeker'</script>'''


@app.route('/unblock_jobseeker', methods=['get', 'post'])
def unblock_jobseeker():
    id = request.args.get('id')
    cmd.execute("update login set login.type='jobseeker' where id='" + str(id) + "'")
    con.commit()
    return '''<script>alert('Jobseeker unBlocked');window.location='/manage_job_seeker'</script>'''


@app.route('/verify_employer')
def verify_employer():
    cmd.execute(
        "SELECT `employer`.*,`login`.* FROM `login` JOIN `employer` ON `employer`.`login_id`=`login`.`id` WHERE `login`.`type`='pending'")
    result = cmd.fetchall()

    return render_template('Admin/verify_employer.html', val=result)


@app.route('/accept_employer', methods=['get', 'post'])
def accept_employer():
    id = request.args.get('id')
    cmd.execute("update login set login.type='employer' where id='" + str(id) + "'")
    con.commit()
    return '''<script>alert('Employer Accepted');window.location='/verify_employer'</script>'''


@app.route('/reject_employer', methods=['get', 'post'])
def reject_employer():
    id = request.args.get('id')
    cmd.execute("delete from login where id='" + str(id) + "'")
    cmd.execute("delete from employer where login_id='" + str(id) + "'")
    con.commit()
    return '''<script>alert('Employer Deleted');window.location='/verify_employer'</script>'''


@app.route('/view_job_req')
def view_job_req():
    cmd.execute("select * from job")
    result = cmd.fetchall()

    return render_template('Admin/view_job_req.html', val=result)


@app.route('/view_admin_feedback', methods=['post'])
def view_admin_feedback():
    type = request.form['select']
    cmd.execute(
        "SELECT `login`.`username`,`feedback`.* FROM `feedback` JOIN `login` ON `login`.`id`=`feedback`.`login_id` WHERE `login`.`type`='" + type + "'")
    s = cmd.fetchall()
    return render_template('Admin/view_feedback.html', val=s)


@app.route('/feedback_admin')
def feedback_admin():
    return render_template('Admin/view_feedback.html')


@app.route('/delete_feedback', methods=['post', 'get'])
def delete_feedback():
    id = request.args.get('id')
    cmd.execute("DELETE`feedback` FROM `feedback` WHERE `id`='" + id + "'")
    con.commit()
    return '''<script>alert('feedback deleted');window.location='/feedback_admin'</script>'''


@app.route('/complaint_admin')
def complaint_admin():
    return render_template('Admin/view_complaint.html')


@app.route('/view_admin_complaint', methods=['post'])
def view_admin_complaint():
    type = request.form['select']
    cmd.execute(
        "SELECT `login`.`username`,`complaint`.* FROM `complaint` JOIN `login` ON `login`.`id`=`complaint`.`login_id` WHERE `login`.`type`='" + type + "'")
    s = cmd.fetchall()
    return render_template('Admin/view_complaint.html', val=s)


@app.route('/delete_complaint', methods=['post', 'get'])
def delete_complaint():
    id = request.args.get('id')
    cmd.execute("DELETE`complaint` FROM `complaint` WHERE `id`='" + id + "'")
    con.commit()
    return '''<script>alert('complaint deleted');window.location='/complaint_admin'</script>'''


@app.route('/reply_complaint_admin')
def reply_complaint_admin():
    id = request.args.get('id')
    session['cid'] = id
    return render_template('Admin/reply_complaint.html')


@app.route('/update_complaint_admin', methods=['post', 'get'])
def update_complaint_admin():
    msg = request.form['textfield']
    cmd.execute("UPDATE complaint SET reply= '" + msg + "' WHERE id='" + str(session['cid']) + "'")
    con.commit()
    return '''<script>alert('Replied');window.location='/complaint_admin'</script>'''


@app.route('/employer_register')
def employer_register():
    return render_template('employer_register.html')


@app.route('/add_employer', methods=['post'])
def add_employer():
    cmp = request.form['textfield']
    usr = request.form['textfield6']
    pwd = request.form['textfield7']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    contact = request.form['textfield5']
    cmd.execute("INSERT INTO login (username,password,type) values ('" + usr + "','" + pwd + "','pending')")
    id = con.insert_id()
    cmd.execute(
        "INSERT INTO employer (company,place,post,pin,contact,login_id) values ('" + cmp + "','" + place + "','" + post + "','" + pin + "','" + contact + "','" + str(
            id) + "')")
    con.commit()
    return '''<script>alert('Employer registered');window.location='/'</script>'''


@app.route('/employer_home')
def employer_home():
    return render_template('Employer/employer_home.html')


@app.route('/job_register')
def job_register():
    cmd.execute("SELECT * from employer")
    s = cmd.fetchall()
    return render_template('Employer/job_register.html', val=s)


@app.route('/add_job', methods=['post', 'get'])
def add_job():
    job = request.form['textfield']
    sal = request.form['textfield3']
    place = request.form['textfield4']
    contact = request.form['textfield5']
    cmd.execute("INSERT INTO job (job,company_id,salary,place,contact_no) values ('" + job + "','" + str(
        session['lid']) + "','" + sal + "','" + place + "','" + contact + "')")
    con.commit()
    return '''<script>alert('Job added');window.location='/job_register'</script>'''


@app.route('/manage_job')
def manage_job():
    cmd.execute(
        "SELECT `job`.*,`employer`.`company` FROM `employer` JOIN `job` ON `job`.`company_id`=`employer`.`login_id`")
    s = cmd.fetchall()
    return render_template('Employer/manage_job.html', val=s)


@app.route('/edit_job', methods=['get'])
def edit_job():
    id = request.args.get('id')
    session['id'] = id
    cmd.execute("SELECT * FROM `job` WHERE `job`.`id`='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template('Employer/edit_job.html', val=s)


@app.route('/update_job', methods=['post'])
def update_job():
    job = request.form['textfield']
    sal = request.form['textfield3']
    place = request.form['textfield4']
    contact = request.form['textfield5']
    cmd.execute(
        "UPDATE job SET `job`= '" + job + "',`salary`='" + sal + "',`place`='" + place + "',`contact_no`= '" + contact + "' WHERE id='" + str(
            session['id']) + "'")
    con.commit()
    return '''<script>window.location='/manage_job'</script>'''


@app.route('/delete_job', methods=['get'])
def delete_job():
    id = request.args.get('id')
    cmd.execute("delete from job where id='" + str(id) + "'")
    con.commit()
    return '''<script>alert('job Deleted');window.location='/manage_job'</script>'''


@app.route('/complaint_employer')
def complaint_employer():
    cmd.execute(
        "SELECT `login`.`username`,`complaint`.* FROM `complaint` JOIN `login` ON `login`.`id`=`complaint`.`login_id` WHERE `login`.`type`='jobseeker'")
    s = cmd.fetchall()
    return render_template('Employer/view_complaint.html', val=s)


@app.route('/reply_complaint_employer', methods=['get'])
def reply_complaint_employer():
    id = request.args.get('id')
    session['cid'] = id
    return render_template('Employer/reply_complaint.html')


@app.route('/update_complaint_employer', methods=['get', 'post'])
def update_complaint_employer():
    msg = request.form['textfield']
    cmd.execute("UPDATE complaint SET reply= '" + msg + "' WHERE id='" + str(session['cid']) + "'")
    con.commit()
    return '''<script>alert('Replied');window.location='/complaint_employer'</script>'''


@app.route('/feedback_employer')
def feedback_employer():
    cmd.execute(
        "SELECT `login`.`username`,`feedback`.* FROM `feedback` JOIN `login` ON `login`.`id`=`feedback`.`login_id` WHERE `login`.`type`='jobseeker'")
    s = cmd.fetchall()
    return render_template('Employer/view_feedback.html', val=s)

#Android webservice

@app.route('/log_in', methods=['post', 'get'])
def log_in():
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