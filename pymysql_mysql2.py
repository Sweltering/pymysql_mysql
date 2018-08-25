import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', database='pymysql_demo', port=3306)  # 连接数据库
cursor = conn.cursor()

# 1、插入数据
# sql = 'insert into user(username, age, password) values ("tom", 23, "tom")'
# cursor.execute(sql)  # 执行SQL语句
# conn.commit()  # 提交数据到数据库

# 通过变量插入值
# sql = 'insert into user(username, age, password) values (%s, %s, %s)'
# username = 'jerry'
# age = 21
# password = 'jerry'
# cursor.execute(sql, (username, age, password))  # 执行SQL语句
# conn.commit()  # 提交数据到数据库


# 2、查找数据
# fetchone函数    返回一条数据
# sql = 'select username,age from user where id=2'
# sql = 'select * from user'
# cursor.execute(sql)
# while True:
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break

# fetchall函数    返回所有数据
# sql = 'select * from user'
# cursor.execute(sql)
# results = cursor.fetchall()  # 返回一个元组
# for result in results:
#     print(result)

# fetchmany函数   自己制定返回几条数据
# sql = 'select * from user'
# cursor.execute(sql)
# results = cursor.fetchmany(2)
# for result in results:
#     print(result)


# 3、删除数据
# sql = 'delete from user where id=2'
# cursor.execute(sql)
# conn.commit()


# 4、更新数据
sql = 'update user set username="hy" where id=3'
cursor.execute(sql)
conn.commit()

conn.close()  # 关闭连接
