# 链接数据库获取信息并返回
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='admin',
                     password='123456',
                     database='test')

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行sql查询
cursor.execute("select VERSION()")

# 使用fetchone()方法获取单挑数据
data=cursor.fetchone()

# 关闭数据库连接
db.close()
