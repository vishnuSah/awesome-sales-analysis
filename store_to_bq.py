from google.cloud import bigquery
import pandas as pd 
import os
import pandas_gbq 

file_path="datasets\\Australia.csv"

# df = pd.read_csv(file_path)
# print(df.head())

df = pd.DataFrame({"Name":["Raj"],
                   "Age": [34],
                   "City": ["NY"] })

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "service-account.json"

client = bigquery.Client()

# sunny-diorama-440117-b0.demodataset.sales
# sunny-diorama-440117-b0.sales_analysis.Australia
project_id = "sunny-diorama-440117-b0"
dataset_id = "sunny-diorama-440117-b0.sales_analysis"
table_id = "Canada"

table_ref = f"{dataset_id}.{table_id}"


try:
    table = client.get_table(table_ref)
    print("table exist")
    df.to_gbq(table_ref, project_id=project_id, if_exists="append")
    print(f"data inserted to {table_ref}")
except:
    print("table does not exist")
    schema = [
        bigquery.SchemaField('Name', "STRING"),
        bigquery.SchemaField('Age', "INTEGER"),
        bigquery.SchemaField('City', "STRING"),
    ]
    table = bigquery.Table(table_ref=table_ref, schema=schema)
    table = client.create_table(table)
    print(f"New table created:: {table}")


