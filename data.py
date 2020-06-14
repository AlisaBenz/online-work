
import mysql.connector
con = mysql.connector.connect(user='alisa', password='',
                              host='127.0.0.1',
                              database='data')
add_db = "insert into record(ID_SENSOR,PM2_5,PM1,PM10,UV,Humi,Temp) values('1','3','5','6','5','7','8')"
cursor = con.cursor()
cursor.execute(add_db)
con.commit()
con.close()
