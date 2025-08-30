import pyodbc 
conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    r"Server=.\SQLEXPRESS;"
    "Database=EMS;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
cursor=conn.cursor()
cursor.execute('''
IF OBJECT_ID('Employees', 'U') IS NULL
CREATE TABLE Employees (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100) NOT NULL,
    department NVARCHAR(100) NOT NULL,
    salary INT NOT NULL
)
''')

conn.commit()
conn.close()