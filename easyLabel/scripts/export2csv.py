"""
将数据库中打好标签的数据导出为csv格式
以 # 作为注释符号
"""
import sqlite3
import csv

inpsql3 = sqlite3.connect('../db.sqlite3')
sql3_cursor = inpsql3.cursor()
sql3_cursor.execute('SELECT * FROM tag_picture WHERE label1_id is not NULL')
#print(sql3_cursor.fetchall())
with open('output.csv','w',newline='') as out_csv_file:
  csv_out = csv.writer(out_csv_file)
  # write header
  csv_out.writerow([d[0] for d in sql3_cursor.description])
  # write data
  for result in sql3_cursor:
    csv_out.writerow(result)
inpsql3.close()