import pymysql.cursors
def mysqldome():


    connection=pymysql.connect(host='192.168.1.249',
                               port=3306,
                               user='root',
                               password='root',
                               db='weixin_platform',
                               charset='utf8',)

    cur=connection.cursor()

    sql="select * from weixin_users"

    cur.execute(sql)
    # 获取剩余结果的第一行数据
    row1 = cur.fetchone()
    print(row1)

    # 获取剩余结果所有数据
    rows=cur.fetchall()
    for dr in rows:
        print(dr)

    cur.close()
    connection.close()