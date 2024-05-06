
import duckdb

sql = '''
COPY (select count(*) from read_parquet("/duckdb/data/*.parquet")) TO 'duckdb/data/result-snappy.parquet' (FORMAT 'parquet'); 
'''

cursor = duckdb.connect()
print(cursor.execute(sql).fetchall())


