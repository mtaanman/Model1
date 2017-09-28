import pandas as pd
from pandas.io import gbq

query = """SELECT * FROM [ziggo-big-query:Menno.pr_train] LIMIT 10"""

try:
	data = gbq.read_gbq(query)
except:
	print 'Query error'

for row in data:
	print(row)