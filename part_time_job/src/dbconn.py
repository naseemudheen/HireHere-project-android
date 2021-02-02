# import pymysql
#
# def iud(qry,vals):
#     con = pymysql.connect(host='localhost',user='root', passwd='',port=3306,db='part_time_job')
#     cmd = con.cursor()
#     cmd.execute(qry,vals)
#     con.commit()
#     con.close()
#
# def selectone(qry):
#     con =pymysql.connect(host='localhost',user='root',passwd='',port=3306,db='part_time_job')
#     cmd = con.cursor()
#     cmd.execute(qry)
#     res=selectone(qry)
#     con.commit()
#     con.close()
#     return res
#
# def selectall(qry):
#     con = pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='part_time_job')
#     cmd = con.cursor()
#     res=selectall(qry)
#     cmd.commit()
#     con.close()
#     return res
#
