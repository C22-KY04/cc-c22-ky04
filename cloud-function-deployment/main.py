import os
import functions_framework
from datetime import datetime
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccountKey.json"

def upload_to_bucket(bucket_name, source_file, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.upload_from_string(
        source_file.read(),
        content_type=source_file.content_type
    )

    return blob.public_url

@functions_framework.http
def handle_http_method(request):
    bucket_name = "my-bucket-24052022"

    source_file = request.files["file"]

    now = datetime.now()
    dt_string = now.strftime("%d%m%Y-%H%M%S")
    blob_name = "images/{}".format(dt_string)

    public_url = upload_to_bucket(bucket_name, source_file, blob_name)

    return public_url

# functions-framework --target handle_http_method --debug