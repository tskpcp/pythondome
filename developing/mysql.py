import pymysql.cursors
def mysqldome():


    connection=pymysql.connect(host='192.168.1.249',
                               port=3306,
                               user='root',
                               password='root',)
    cur=connection.cursor()
    connection.set_charset("utf8")
    connection.select_db("pythontest")
    sql="select * from cms_admin_mst"

    cur.execute(sql)
    # 获取剩余结果的第一行数据
    row1 = cur.fetchone()
    print(row1)

    # 获取剩余结果所有数据
    rows=cur.fetchall()
    for dr in rows:
        print("fetchall"+dr)




    cur.close()
    connection.close()