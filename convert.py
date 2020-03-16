import pymysql,redis

mysql_user = "root"
mysql_password = "root12345"
redis_password = "12345"
#change value of other variables like host, port and db_name according to your usecase
conn = pymysql.connect( host='0.0.0.0',port=3307,user=mysql_user,
                        password=mysql_password,db='db_name',charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

sql = 'select  word,definition from db_table '

cursor = conn.cursor()

cursor.execute(sql)

result = cursor.fetchall()
conn.close()
d={}

for el in result:
    d[  el["word"].lower()  ] = el["definition"].lower()


r = redis.Redis( host='localhost',port=6379,password=redis_password)
r.mset(d)
r.close()
