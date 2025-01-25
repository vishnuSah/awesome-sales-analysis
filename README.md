The project is about ETL process (end-to-end) where we will upload data on Flask web portal then we will store that data in Warehouse (google Bigquery) and do business analysis in Looker Studio. <br>

Upload File -> Google Cloud Storage -> Cloud Function -> Bigquery -> Looker Studio

<br><br> File Upload Portal <br><br> 
<img width="935" alt="image" src="https://github.com/user-attachments/assets/62f8397b-d11f-495a-8c5e-63248d001288" />

<br><br> Bigquery Table <br><br> 
<img width="860" alt="image" src="https://github.com/user-attachments/assets/269af05b-9505-47d4-9b05-8ff652f7dc13" />


<br><br> Looker Business Analysis <br><br> 
<img width="448" alt="image" src="https://github.com/user-attachments/assets/1944c521-d181-40ec-b944-b4be275508ed" />

<br><br>
How to Run Code in Local <br>

1. Clone Project <br>
2. Make google account <br>
3. Download service account json file and place in main folder <br>
4. Create new cloud storage bucket, Bigquery table with same columns as dataset columns <br>
5. Place bucket name in main.py and BQ table name in gcs_to_bq.py file <br>
6. Create Cloud Function with storage trigger(bucket you created) and place gcs_to_bq.py code <br>
7. Run main.py, access browser on port 5000, upload file and check BQ table for data <br>
8. (Most Important) IF error occurred, Google iT !! <br>
