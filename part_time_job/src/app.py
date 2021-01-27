from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login',methods=['post'])
def login():
    uname = request.form['textfield']
    passwd = request.form['textfield2']
    print(uname)


@app.route('/admin_home')
def admin_home():
    return render_template('Admin/admin.html')

@app.route('/manage_job_seeker')
def manage_job_seeker():
    return render_template('Admin/manage_job_seeker.html')

@app.route('/verify_employer')
def verify_employer():
    return render_template('Admin/verify_employer.html')

@app.route('/complaint_admin')
def complaint_admin():
    return render_template('Admin/view_complaint.html')

@app.route('/feedback_admin')
def feedback_admin():
    return render_template('Admin/view_feedback.html')

@app.route('/view_job_req')
def view_job_req():
    return render_template('Admin/view_job_req.html')

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