import pymysql
from flask import *

from dbconn import *
app = Flask(__name__)
con = pymysql.connect(host='localhost',user='root', passwd='',port=3306,db='part_time_job')
cmd = con.cursor()

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login',methods=['post','get'])
def login():
    uname = request.form['textfield']
    passwd = request.form['textfield2']
    cmd.execute("select * from login where username='"+uname+"' and password ='"+passwd+"'")
    res =cmd.fetchone()
    print(res)
    if res is None:
        return "<script> alert('invalid username or password')</script>"
    else:
        if res[3]=='admin':
            return '''<script>alert('login succesfull admin');window.location='/admin_home' </script>'''
        else:
            return "<script> alert('invalid username or password')</script>"




@app.route('/admin_home')
def admin_home():
    return render_template('Admin/admin.html')

@app.route('/manage_job_seeker')
def manage_job_seeker():
    return render_template('Admin/manage_job_seeker.html')

@app.route('/verify_employer')
def verify_employer():
    cmd.execute("SELECT `employer`.*,`login`.* FROM `login` JOIN `employer` ON `employer`.`login_id`=`login`.`id` WHERE `login`.`type`='pending'")
    result =cmd.fetchall()

    return render_template('Admin/verify_employer.html',val=result)

@app.route('/accept_employer',methods=['get','post'])
def accept_employer():
    id =request.args.get('id')
    cmd.execute("update login set login.type='employer' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('Employer Accepted');window.location='/verify_employer'</script>'''

@app.route('/reject_employer',methods=['get','post'])
def reject_employer():
    id =request.args.get('id')
    cmd.execute("delete from login where id='"+str(id)+"'")
    cmd.execute("delete from employer where login_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('Employer Deleted');window.location='/verify_employer'</script>'''


@app.route('/view_job_req')
def view_job_req():
    cmd.execute("select * from job")
    result = cmd.fetchall()

    return render_template('Admin/view_job_req.html',val=result)



@app.route('/complaint_admin')
def complaint_admin():
    return render_template('Admin/view_complaint.html')

@app.route('/reply_complaint_admin')
def reply_complaint_admin():
    return render_template('Admin/reply_complaint.html')

@app.route('/feedback_admin')
def feedback_admin():
    return render_template('Admin/view_feedback.html')

@app.route('/reply_feedback_admin')
def reply_feedback_admin():
    return render_template('Admin/reply_feedback.html')



@app.route('/employer_register')
def employer_register():
    return render_template('employer_register.html')

@app.route('/employer_home')
def employer_home():
    return render_template('Employer/employer_home.html')

@app.route('/job_register')
def job_register():
    return render_template('Employer/job_register.html')

@app.route('/manage_job')
def manage_job():
    return render_template('Employer/manage_job.html')

@app.route('/complaint_employer')
def complaint_employer():
    return render_template('Employer/view_complaint.html')

@app.route('/feedback_employer')
def feedback_employer():
    return render_template('Employer/view_feedback.html')





app.run(debug=True)