from pyspark.sql import SQLContext, SparkSession
import read

spark = SparkSession.Builder().appName('rdd').master('local').getOrCreate()

# conn = read.mysql(     host='127.0.0.1',
#                        user='root',             # 数据库用户名
#                        passwd='yy101597wei',    # 密码
#                        db='mysql_test',         # 数据库名称
#                        table = 'student',
#                        port=3306,
#                        charset='utf8')

p = ['127.0.0.1','root','yy101597wei', 'mysql_test', 'student',3306,'utf8']
data = read.mysql(p)
print(data)

df = spark.createDataFrame(data)    #转换为spakr dataframe
data = df.rdd                       #转换成rdd