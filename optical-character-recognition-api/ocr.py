def url_to_image(url):
    source_file = urllib.request.urlopen(url)
    image = np.asarray(bytearray(source_file.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image

def read_image(image):
    r = 800 / image.shape[0]
    dim = (int(image.shape[1] * r), 800)

    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return image

def preprocessing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = 127
    blackWhite = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]

    kernel = np.ones((3,3), np.uint8)
    img_erosion = cv2.erode(blackWhite, kernel, iterations=1)

    return img_erosion

def get_text(image_procesed):
    result = pytesseract.image_to_string(image_procesed)
    list_value = result.split("\n")

    return list_value

