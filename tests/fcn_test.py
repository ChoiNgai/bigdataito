from pyspark.sql import SQLContext, SparkSession
import read

spark = SparkSession.Builder().appName('bigdataito').master('local').getOrCreate()

data = read.mysql(     host='127.0.0.1',        # 主机地址
                       user='root',             # 数据库用户名
                       passwd='yy101597wei',    # 密码
                       db='mysql_test',         # 数据库名称
                       table = 'student',       # 表名
                       port=3306,             # 端口号
                       charset='utf8'          # 编码格式
                    )

df = spark.createDataFrame(data)    #转换为spakr dataframe
df.show()