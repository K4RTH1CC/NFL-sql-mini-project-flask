import mariadb
conn = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='toor',
         database='nfl')
query = "select * from user"
cur = conn.cursor()
cur.execute(query)
for (user,pw) in cur:
    print(user,pw)