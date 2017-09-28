import uuid

from google.cloud import bigquery 

query = """SELECT * FROM Menno.pr_train LIMIT 10"""
client = bigquery.Client()

query_job = client.run_async_query(str(uuid,uuid4()), query)
query_job.begin()
data = query_job.result()

for row in data:
	print(row)