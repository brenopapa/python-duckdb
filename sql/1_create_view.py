
import duckdb

sql = '''
create view target_data as select * from read_parquet("/duckdb/data/*.parquet");
'''

cursor = duckdb.connect()
print(cursor.execute(sql).fetchall())