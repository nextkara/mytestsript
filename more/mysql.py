import pymysql
try:
    connec = pymysql.connect(host = "192.168.238.128", user = "root", passwd = "root", db = 'person', port = 3306, charset = "utf-8")
    cur = connec.cursor()
    cur.execute("select * from person")
    data = cur.fetchall()
    for d in data:
        print("ID: " + str(d[0]) + " Name: " + d[1] + " Sex : " + d[2])
    cur.close()
    connec.close()
except Exception:
    print("Erorr!")
