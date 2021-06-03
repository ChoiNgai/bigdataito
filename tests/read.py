import pymysql

def mysql(host,user,passwd,db,table,port = 3306,charset = 'utf8'):

    parameter = [host ,user ,passwd ,db ,port ,charset] #合并为数组(否则pymysql读取会报错)
    '''连接数据库'''
    conn = pymysql.connect(host = parameter[0],
                    user = parameter[1],  # 数据库用户名
                    passwd = parameter[2],  # 密码
                    db = parameter[3],  # 数据库名称
                    port = parameter[4],
                    charset= parameter[5]
                    )

    cursor = conn.cursor()  #创建游标对象
    sql = str( "select * from"+' '+ table  )    # 查询表格所有数据
    cursor.execute(sql)
    result = cursor.fetchall()

    return result

