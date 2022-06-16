import os
from datetime import datetime
from flask import Flask, jsonify, request
from middleware import is_authenticated
from modules.storage.function import upload_to_bucket, download_from_bucket, delete_from_bucket
from modules.ocr.function import extract_text_from_image
from modules.classification.function import image_classification

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET"])
def base_url():
    return "Hello from Optical Character Recognition API, C22-KY04."

@app.route("/ocr", methods=["POST"])
@is_authenticated
def optical_character_recognition():
    if "file" not in request.files:
        return jsonify({
            "status": "Bad Request",
            "message": "No file part."
        }), 400

    source_file_name = request.files.get("file")

    if source_file_name.filename == "":
        return jsonify({
            "status": "Bad Request",
            "message": "No selected file."
        }), 400

    if not (source_file_name and allowed_file(source_file_name.filename)):
        return jsonify({
            "status": "Not Acceptable",
            "message": "Only files with extension png, jpg, jpeg are allowed."
        }), 406

    bucket_name = "id-cards-photo"
    blob_name = datetime.now().strftime("%d%m%Y-%H%M%S")
    destination_blob_name = "{}.png".format(blob_name)
    public_url = upload_to_bucket(bucket_name, source_file_name, destination_blob_name)

    source_blob_name = "{}.png".format(blob_name)
    destination_file_name = "tmp/image.png"
    download_from_bucket(bucket_name, source_blob_name, destination_file_name)

    is_id_card = image_classification()

    if not is_id_card:
        return jsonify({
            "status": "Not Acceptable",
            "message": "That's not an Indonesian ID Card (KTP). Please try again."
        }), 406

    try:
        data = extract_text_from_image(public_url)

        return jsonify({
            "status": "OK",
            "message": "Successfully extract data with OCR.",
            "data": data
        }), 200
    except Exception as e:
        message = str(e)

        delete_from_bucket(bucket_name, source_blob_name)

        return jsonify({
            "status": "Internal Server Error",
            "message": message
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
