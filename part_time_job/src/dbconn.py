import pymysql

def iud(qry,vals):
    con = pymysql.connect(host='localhost',
                      user='root', passwd='',
                      port=3306,db='part_time_job')
    cmd = con.cursor()
    cmd.execute(qry,vals)
    con.commit()
    con.close()