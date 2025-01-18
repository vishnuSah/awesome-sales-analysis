import functions_framework
from google.cloud import bigquery
from google.cloud import storage 
import pandas as pd 
from io import StringIO

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    # event_id = cloud_event["id"]
    # event_type = cloud_event["type"]

    bucket = data["bucket"]
    filename = data["name"]

    gcs_client = storage.Client()
    bucket = gcs_client.get_bucket(bucket)
    blob = bucket.blob(filename)
    data = blob.download_as_bytes().decode('utf-8')

    df = pd.read_csv(StringIO(data))
    df['ORDERDATE'] = df['ORDERDATE'].apply(lambda x: x.split()[0].replace('/','-'))
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], format="%m-%d-%Y")
    # print(df.head())
    insert_to_bq(df)

    print("Success")

def insert_to_bq(df):
    # print(df.dtypes)
    

    table_id = "sunny-diorama-440117-b0.sales_analysis.sales_data_latest"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",  # Replace with "WRITE_TRUNCATE" if needed
    )

    bq_client = bigquery.Client()
    job = bq_client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Wait for the job to complete

    print(f"Uploaded {len(df)} rows to {table_id}.")
    


