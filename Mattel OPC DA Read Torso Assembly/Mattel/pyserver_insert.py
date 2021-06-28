import pyodbc 
conn = pyodbc.connect(driver='{SQL Server}', host='WCKR00157338\SQLEXPRESS', database='TA', user='sa', password='Mattel@123')

cursor = conn.cursor()
cursor.execute("INSERT INTO [dbo].[trial](tes,tes2) VALUES(?, ?)", 10, 'WOW')
conn.commit() #you should commit the execute conn to write data to Server
