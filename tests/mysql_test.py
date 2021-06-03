import pymysql

'''连接数据库'''
conn = pymysql.connect(host='127.0.0.1',
                       user='root',  # 数据库用户名
                       passwd='yy101597wei',  # 密码
                       db='mysql_test',  # 数据库名称
                       # port=3306,
                       #charset='utf8'
                       )

cursor = conn.cursor()  #创建游标对象

sql = "select * from student"
cursor.execute(sql)
List = cursor.fetchall()

print(List)