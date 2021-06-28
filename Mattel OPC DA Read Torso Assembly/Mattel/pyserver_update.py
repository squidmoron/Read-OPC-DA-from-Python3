import pyodbc 
conn = pyodbc.connect(driver='{SQL Server}', host='WCKR00157338\SQLEXPRESS', database='TA', user='sa', password='Mattel@123')

cursor = conn.cursor()
cursor.execute("UPDATE [TA].[dbo].[trial] SET tes2 = 'wow' WHERE tes = 10;")
conn.commit()
