import pg8000
conn = pg8000.connect(host='192.168.1.103', user='admin', password='Cisc0123', database='qytangdb')
cursor = conn.cursor()
cursor.execute('create table test1(t1 int,t2 varchar(40))')
cursor.execute("insert into test1(t1,t2) values (11,'welcome to qytang')")
cursor.execute("insert into test1(t1,t2) values (12,'welcome to python')")
cursor.execute('select * from test1')
yourresults = cursor.fetchall()
for i in yourresults:
    print(i)
if __name__ == '__main__':
    pass