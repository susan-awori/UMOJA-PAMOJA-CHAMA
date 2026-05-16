from google.cloud import storage

def upload_to_chama_bucket(bucket_name, source_file, destination_blob):
    """Uploads a local file directly to the secure cloud storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    
    blob.upload_from_filename(source_file)
    print(f" Successfully uploaded {source_file} to gs://{bucket_name}/{destination_blob}")

# Execute the uploads to their respective data folders
bucket = "chama-001"

# Uploading the Unstructured Bylaws
upload_to_chama_bucket(bucket, "bylaws.md", "bylaws/bylaws.md")

# Uploading the Structured M-Pesa Financial Ledger PDF
upload_to_chama_bucket(bucket, "umoja_chama_mpesa_statement.pdf", "mpesa/umoja_chama_mpesa_statement.pdf")