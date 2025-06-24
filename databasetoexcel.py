import pandas as pd
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',       #your database name
                             password='root',      #your database password
                             database='employees')  #your data base name

query = "SELECT * FROM emp" #your table name

data = pd.read_sql(query, connection)

connection.close()

data.to_excel('output.xlsx', index=False)