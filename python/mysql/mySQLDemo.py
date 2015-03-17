from mySQL import *

def selectDemo(mysql, database):
   query = "select * from %s_users" %database.prefix

   try:
       result = mysql.select(query)
       if len(result) == 0:
           print "No record"
       else:
           print "%d record(s)" %len(result)
   except:
       print "MySQL select exception: %s" %query


if __name__ == '__main__':
    localDatabase = myDatabase('q40x7', 'localhost', 'root','chen1146','signaltest')
    
    mysql = mySQL(localDatabase.host, localDatabase.username,localDatabase.password, localDatabase.database)
    
    selectDemo(mysql, localDatabase)