import os
from datetime import datetime
from google.cloud import storage
from flask import Flask, jsonify, request
from modules.ocr.function import extract_text_from_image
from modules.identify.function import doidentify

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tesseract-container-53596ccdac20.json"

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def upload_to_bucket(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(
        source_file_name.read(),
        content_type=source_file_name.content_type
    )

    return blob.public_url

@app.route("/", methods=["GET", "POST"])
def optical_character_recognition():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({
                "status": "Bad Request",
                "message": "No file part."
            }), 400

        source_file_name = request.files["file"]

        if source_file_name.filename == "":
            return jsonify({
                "status": "Bad Request",
                "message": "No selected file."
            }), 400

        bucket_name = "my-bucket-05062022"
        destination_blob_name = "{}.png".format(datetime.now().strftime("%d%m%Y-%H%M%S"))
        public_url = upload_to_bucket(bucket_name, source_file_name, destination_blob_name)

        judge = doidentify(public_url)
        if judge == 'nonktp':
            return jsonify({
                "status": "Not Acceptable",
                "message": "That's not an Indonesian ID Card (KTP). Please try again."
            }), 406

        data = extract_text_from_image(public_url)

        return jsonify({
            "status": "OK",
            "message": "Successfully extract data with OCR.",
            "data": data
        }), 200

        # return jsonify({
        #     "status": "OK",
        #     "message": "File has been uploaded to Google Cloud Storage.",
        #     "data": public_url
        # }), 200
    
    else:
        return "Hello from Optical Character Recognition API, C22-KY04."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
