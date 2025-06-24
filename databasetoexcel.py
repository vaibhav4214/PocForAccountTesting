import pandas as pd
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='employees')

query = "SELECT * FROM emp"

data = pd.read_sql(query, connection)

connection.close()

data.to_excel('output.xlsx', index=False)