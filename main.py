from flask import Flask, render_template, request, redirect, url_for, flash
from google.cloud import storage
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Configure Google Cloud Storage bucket name
GCS_BUCKET_NAME = "vs-cloudbucket-1"  # Replace with your GCS bucket name

# Configure Google Cloud authentication (set environment variable for service account key)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "service-account.json"

# Route for the home page with the file upload form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part in the request')
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash('No file selected for uploading')
        return redirect(url_for('index'))

    try:
        # Upload file to GCS
        storage_client = storage.Client()
        bucket = storage_client.bucket(GCS_BUCKET_NAME)
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file, content_type=file.content_type)

        flash(f'File {file.filename} uploaded successfully to GCS bucket {GCS_BUCKET_NAME}')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'An error occurred: {e}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
