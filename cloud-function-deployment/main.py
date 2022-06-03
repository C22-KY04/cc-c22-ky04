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

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )


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