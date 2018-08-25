# pymysql驱动连接数据库

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', database='pymysql_demo', port=3306)  # 连接数据库
cursor = conn.cursor()  # 创建一个游标

cursor.execute('select 1')  # 通过游标执行查询语句
result = cursor.fetchone()
print(result)

conn.close()  # 关闭连接