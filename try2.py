# Below Code snippet is check the existence of database in the SQL Server
import pyodbc
server = 'Mypc'
username = 'sa'
password = 'Windows1'
new_database = 'cpp_db'
#Connecting to MS SQL Server
connection = None
try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                'SERVER='+server+';UID='+username+
                                ';PWD='+ password)
    print('Connected to SQL Server Successfully')
except:
    print('Connection failed to SQL Server')

if connection is not None:
    connection.autocommit = True

#Asking user to enter database name he wants to check
database_name = input('Enter database name to check exist or not: ')

cur = connection.cursor()
cur.execute("SELECT name FROM master.dbo.sysdatabases where name=?;",(database_name,))
data=cur.fetchall()

print(data)

#Printing if database exists or not
if not data:
    print("'{}' Database does not exist.".format(database_name))
else:
    print("'{}' Database already exists".format(database_name))

# After all operation is done close the database connection and cursor
cusor.close()
connection.close()
print('Done')
