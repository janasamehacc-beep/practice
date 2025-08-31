import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    r"Server=.\SQLEXPRESS;"
    "Database=EMS;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

# cursor.execute(''' ALTER TABLE Employees 
#                ADD manager_id INT 
#                 REFERENCES Managers(id)
# ''')
# cursor.execute(''' SELECT * FROM Employees JOIN Managers ON Employees.manager_id = Managers.id ''')

# cursor.execute(''' INSERT INTO Employees ( name,department, salary, manager_id) 
#                 VALUES ( 'John Jay', 'IT', 60000, 1), 
#                 ( 'Jane Doe', 'HR', 55000, 2),
#                 ( 'Mike Smith', 'Finance', 70000, 1),
#                 ( 'Emily Davis', 'IT', 65000, 1),
#                 ('Sarah Johnson', 'Marketing', 60000, 3) 
#                 ''')
# cursor.execute(''' SELECT * FROM Employees ''')
cursor.execute(''' UPDATE Employees
SET salary = 1000
WHERE name = 'John Jay';
 ''')
conn.commit() 
conn.close()
