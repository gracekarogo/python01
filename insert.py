import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT  INTO EMPLOYEES VALUES (11, 'FAITH KARAMI', 34, 450000.00)")

conn.execute("INSERT  INTO EMPLOYEES VALUES (32, 'JANE NJOROGE', 25, 450000.00)")

conn.execute("INSERT  INTO EMPLOYEES VALUES (38, 'TRAVIS SCOTT', 45, 4560000.00)")

conn.execute("INSERT  INTO EMPLOYEES VALUES (6, 'ETHAN HOOVER', 34, 49000.00)")

conn.execute("INSERT  INTO EMPLOYEES VALUES (54, 'FRIDAH KARAMI', 26, 450000.00)")

conn.commit()
print("Records inserted successfuy")
conn.close()