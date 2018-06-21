import pymysql
class mySqlDBHelper:
    myVersion=0.1
    #初始化
    def __init__(self,host,port,user,password,charset):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.charset=charset

        try:
            self.connection=pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password)
            self.connection.set_charset("utf8")
            self.cursor=self.connection.cursor()
        except pymysql.Error as e:
            print('mysql init error :%d %s'%(e.args[0],e.args[1]))
    #数据库表明
    def setDB(self,db):
        try:
            self.connection.select_db(db)
        except pymysql.Error as e:
            print('mysql setDB error :%d %s' % (e.args[0], e.args[1]))
    #获取sql语句
    def query(self,sql):
        try:
            rows=self.cursor.execute(sql)
            return rows;
        except pymysql.Error as e:
            print('mysql query error :%s SQL:%s' % (e,sql))

    # 获取剩余结果的第一行数据
    def queryOnlyRow(self,sql):
        try:
            self.query(sql)
            result=self.cursor.fetchone()
            desc=self.cursor.description
            row={}
            for i in range(0,len(result)):
                row[desc[i][0]]=result[i]
            return row;
        except pymysql.Error as e:
            print('mysql query error :%s SQL:%s' % (e, sql))

    # 获取剩余结果前n行数据
    def quertFetchmanyRow(self,sql,n):
        try:
            self.query(sql)
            result=self.cursor.fetchmany(n)
            desc=self.cursor.description
            rows=[]
            for cloum in result:
                row={}
                for i in range(0,len(cloum)):
                    row[desc[i][0]]=cloum[i]
                rows.append(row)
            return  rows
        except pymysql.Error as e:
            print('mysql query error :%s SQL:%s' % (e, sql))
    #全部查询
    def queryAll(self,sql):
        try:
            self.query(sql)
            result=self.cursor.fetchall()
            desc=self.cursor.description
            rows=[]
            for cloumn in result:
                row={}
                for i in range(0,len(cloumn)):
                    row[desc[i][0]]=cloumn[i]
                rows.append(row)
            return  rows;
        except pymysql.Error as e:
            print('mysql query error :%s SQL:%s' % (e, sql))
    # 调用无参存储过程

    def getCall(self, procName):
         try:
            cursor=self.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.callproc(procName)
            result=cursor.fetchall()
            desc=self.cursor.description
            rows=[]
            for cloumn in result:
                row={}
                for i in range(0,len(cloumn)):
                    row[desc[i][0]]=cloumn[i]
                rows.append(row)
            return  rows;
         except pymysql.Error as e:
            print('mysql getCall error :%s %s' % (e.args[0], e.args[1]))


    # 调用有参存储过程
    def getCallParmar(self,procName,pData):
            try:
                cursor = self.cursor(cursor=pymysql.cursors.DictCursor)
                cursor.callproc(procName,args= '('+pData+')')
            except pymysql.Error as e:
                print('mysql getCallParmar error :%s %s' % (e.args[0], e.args[1]))
    #添加
    def insert(self,tableName,pData):
        try:
            newData={}
            for key in pData:
                newData[key]="'"+pData[key]+"'"
            key=','.join(newData.keys())
            value=','.join(newData.values())
            sql="insert into "+tableName+"("+key+") values("+value+")"
            self.query("set names 'utf8'")
            self.query(sql)
            self.commit()
        except pymysql.Error as e:
            self.connection.rollback()
            print('mysql insert error :%s %s' % (e.args[0], e.args[1]))
        finally:
            self.close()

    #修改
    def update(self,tableName,pData,whereData):
        try:
            newDara=[]
            keys=pData.keys()
            for i in keys:
                item="%s=%s"%(i,"'"+pData[i]+"'")
                newDara.append(item)
            items=','.join(newDara)
            newDara2=[]
            keys=whereData.keys()
            for i in keys:
                item = "%s=%s" % (i,"'" + whereData[i] + "'")
                newDara2.append(item)
            whereItems=" AND ".join(newDara2)
            sql="update "+tableName+" set "+items+" where "+whereItems
            self.query("set names 'utf8'")
            self.query(sql)
            self.commit()
        except pymysql.Error as e:
            self.connection.rollback()
            print('mysql update error :%s %s' % (e.args[0], e.args[1]))
        finally:
            self.close()

    #可以获取到最新自增的ID，也就是最后插入的一条数据ID
    def getLastInsertRowId(self):
        return self.cursor.lastrowid;
    #获取行数
    def getRowCount(self):
        return self.cursor.rowcount;
    #提交
    def commit(self):
        self.connection.commit()
    #关闭
    def close(self):
        self.cursor.close()
        self.connection.close()