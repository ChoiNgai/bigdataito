from pyspark.sql import SQLContext, SparkSession

if __name__ == '__main__':
    
    # # spark 初始化
    # spark = SparkSession. \
    #     Builder(). \
    #     appName('sql'). \
    #     master('local'). \
    #     getOrCreate()
    # # spark = SparkSession.Builder().appName('sql').master('local').getOrCreate()

    # # mysql 配置(需要修改)
    # prop = {'user': 'root', 'password': 'yy101597wei'}
    # # prop = {'user': 'YY_MySQL', 'password': 'yy101597wei', 'driver': 'com.mysql.cj.jdbc.Driver'}

    # # database 地址(需要修改)
    # jdbcurl = 'jdbc:mysql://127.0.0.1:3306/mysql_test'

    # # 读取表
    # data = spark.read.jdbc(url=jdbcurl, table='student', properties=prop)


    # # jdbcDF = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/mysql_test").option("driver","com.mysql.jdbc.Driver").option("dbtable", "student").option("user", "root").option("password", "yy101597wei").load()
    # # jdbcDF.show()

    # # 打印data数据类型
    # print(type(data))

    # # 展示数据
    # data.show()

    # # 关闭spark会话
    # spark.stop()

    spark = SparkSession.Builder().appName('sql').master('local').getOrCreate()
    df = spark.read.format('jdbc').options(url='jdbc:mysql://127.0.0.1',dbtable='mysql_test.student',user='root',password='yy101597wei' ).load()

    df.show()
