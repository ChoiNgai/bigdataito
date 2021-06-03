import pymysql
from pyspark.sql import SparkSession

def mysql(parameter):

    '''连接数据库'''
    conn = pymysql.connect(host = parameter[0],
                       user = parameter[1],  # 数据库用户名
                       passwd = parameter[2],  # 密码
                       db = parameter[3],  # 数据库名称
                       port = parameter[5],
                       charset= parameter[6]
                       )

    cursor = conn.cursor()  #创建游标对象
    table = parameter[4]
    sql = str( "select * from"+' '+ table  )
    cursor.execute(sql)
    result = cursor.fetchall()

    return result