```python
# Vertica is a database.
# For MySQL use: import mysql.connector
from vertica_python import connect
import csv
import pandas as pd

conn_info = {
    'host': '123.45.67.89',
    'port': 5433,
    'user': 'Username',
    'password': 'password',
    'database': 'Schema_name', 
    'read_timeout': 600,       # 10 minutes timeout on queries
    'unicode_error': 'strict', # default throw error on invalid UTF-8 results
    'ssl': False # SSL is disabled by default
    }

connection = connect(**conn_info)

cursor = connection.cursor()

# Execute commands in the database.
cursor.execute("Select * from table_name")

# Fetch all the records and write it to a csv.
with open('output.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in cursor.description])
    for row in cursor.fetchall():
        writer.writerow(row)

# Make a pivot table. 
df = pd.read_csv('output.csv')
df.pivot_table(index=['col_name1'], values='col_name2', columns='col_name3', aggfunc='sum')
```

