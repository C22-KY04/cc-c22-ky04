import os
from flask import Flask
from PIL import Image
from modules.ocr import *

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def hello():
    imgpath = url_to_image("https://storage.googleapis.com/my-bucket-24052022/05062022-060545.png")
    image = read_image(imgpath)
    img_proc = preprocessing(image)
    list_text = get_text(img_proc)

    WORDS = get_counter(path_kata_dasar)

    new_list = processing_word(list_text, WORDS)
    new_value = correction_typo(new_list)
    kabupaten = get_kabupaten(new_value)

    prevalue = txt_to_list('/app/src/key.txt')
    pair = get_pair(prevalue, new_value)
    new_pair = processing_pair(pair, kabupaten)

    new_pair = processing_pair(pair, kabupaten)
    new_pair = get_blood_type(new_pair)
    new_dict = pair_to_JSON(new_pair)

    return new_dict, 200

    # return pytesseract.image_to_string(Image.open('test.png'))

@app.route('/ls')
def test():
    return os.system("ls -la /*")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))