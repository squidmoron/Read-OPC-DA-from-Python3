import pyodbc 
conn = pyodbc.connect(driver='{SQL Server}', host='WCKR00157338\SQLEXPRESS', database='TA', user='sa', password='Mattel@123')

cursor = conn.cursor()
cursor.execute('SELECT TOP (1) [tes],[tes2] FROM [TA].[dbo].[trial]')


for row in cursor:
    print(row)