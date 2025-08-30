import  sqlite3 
connection = sqlite3.connect('EMS.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Managers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL
                )''')
connection.commit()
connection.close()