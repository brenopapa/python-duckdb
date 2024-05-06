
import duckdb

sql = '''
SELECT 1
'''

cursor = duckdb.connect()
print(cursor.execute(sql).fetchall())