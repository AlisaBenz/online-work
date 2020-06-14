import mysql.connector
import urllib.request

con = mysql.connector.connect(
    user='alisa', password='', host='127.0.0.1', database='data')


def insert_data(sensor_id, myfile):
    data = []
    data.append(sensor_id)
    for key, value in myfile.items():
        data.append(value)
    query = "INSERT INTO record (ID_SENSOR,PM2_5,PM1,PM10,UV,Humi,Temp) VALUES('%s','%s','%s','%s','%s','%s','%s')"
    cursor = con.cursor()
    cursor.execute(query, data)
    con.commit()
    con.close()


link = "https://www.aismagellan.io/api/things/pull/3654fa50-5c96-11ea-b7bc-61455edf93af"
f = urllib.request.urlopen(link)
myfile = f.read()
insert_data("1", myfile)
