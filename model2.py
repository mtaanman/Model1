import pandas as pd
from pandas.io import gbq

query = """SELECT * FROM [ziggo-big-query:Menno.pr_train] LIMIT 10"""
pid = 'ziggo-big-query'

try:
	data = gbq.read_gbq(query,project_id=pid)
except:
	print 'Query error'

for row in data:
	print(row)