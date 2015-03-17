import MySQLdb

class myDatabase:
    def __init__(self, pre, h, u, p, db):
        self.prefix=pre
        self.host=h
        self.username=u
        self.password=p
        self.database=db

class mySQL:
    def __init__(self, localhost, username, password, database):
        self.conn = MySQLdb.connect(host=localhost,user=username,passwd=password,db=database,port=3306, charset='utf8')
        self.cur=self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def select(self, sql):
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            return results
        except MySQLdb.Error,e:
            self.printMsg("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            return None

    def update(self, sql):
        try:
            result = self.cur.execute(sql)
            if result != 1:
                self.printMsg('Mysql fail to update.')
            self.conn.commit()
        except MySQLdb.Error,e:
            self.printMsg("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def printMsg(self, msg):
        print msg, sys.exc_info()[0]

