from collections import Counter
import re
import urllib.request
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
import cv2
import json

# Get Image
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

# Pre-Processing Image
def preprocessing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = 127
    blackWhite = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]

    kernel = np.ones((3,3), np.uint8)
    img_erosion = cv2.erode(blackWhite, kernel, iterations=1)

    return img_erosion

# Get Text from Image
def get_text(image_procesed):
    result = pytesseract.image_to_string(image_procesed)
    list_value = result.split("\n")

    return list_value

# Typo Correction
def words(text): return re.findall(r'\w+', text.lower())

path_kata_dasar = '/app/src/katadasar.txt'

def get_counter(path_kata_dasar):
    WORDS = Counter(words(open(path_kata_dasar).read()))
    return WORDS

WORDS = get_counter(path_kata_dasar)

def P(word, N=sum(get_counter(path_kata_dasar).values())):
    # "Probability of `word`."
    return WORDS[word] / N

def correction(word):
    # "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word):
    # "Generate possible spelling corrections for word."
    return (known([word], path_kata_dasar) or known(edits1(word), path_kata_dasar) or known(edits2(word), path_kata_dasar) or [word])

def known(words, path_kata_dasar):
    # "The subset of `words` that appear in the dictionary of WORDS."
    WORDS = get_counter(path_kata_dasar)
    return set(w for w in words if w in WORDS)

def edits1(word):
    # "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)] # [('', 'kemarin'), ('k', 'emarin'), ('ke', 'marin'), dst]
    deletes    = [L + R[1:]               for L, R in splits if R] # ['emarin', 'kmarin', 'kearin', dst]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1] # ['ekmarin', 'kmearin', 'keamrin', dst]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] # ['aemarin', 'bemarin', 'cemarin', dst]
    inserts    = [L + c + R               for L, R in splits for c in letters] # ['akemarin', 'bkemarin', 'ckemarin', dst]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    # "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def processing_word(list_value, WORDS):
    new_list = []
    for string in list_value:
        if string.isspace() or len(string)==0:
            continue
        lower_string = string.lower()
        no_punc_string = re.sub(r'[^\w\s]','', lower_string)
        no_wspace_string = no_punc_string.replace('\n', ' ')
        no_punc_string = re.sub(r'[^\w\s]','', lower_string)
        no_wspace_string = no_punc_string.replace('\n', ' ')
        no_wspace_string = re.sub(' +', ' ', no_wspace_string)
        new_list.append(correction(no_wspace_string))

    return new_list

def correction_typo(new_list):
    new_value = []
    for string in new_list:
        temp = ''
        data = string.split(" ")
        for s in data:
            # print(correction(s))
            temp = temp + " " + correction(s)
        new_value.append(temp[1:])

    return new_value

def get_kabupaten(new_value):
    kabupaten = new_value[1]

    return kabupaten

# Get Value
def txt_to_list(path):
    # opening the file in read mode
    my_file = open(path, "r")
    
    # reading the file
    data = my_file.read()
    
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    data_into_list = data.split("\n")
    my_file.close()
    return data_into_list

def get_pair(prevalue, new_value):
    pair = {}
    for string in new_value:
        temp = string.split(' ')
        new_temp = []
        flag = False
        keyFlag = False
        key = ''
        for word in temp:
            if flag == False and word in prevalue:
                flag = True
                keyFlag = True
                key = word
            if flag and keyFlag:
                pair[key] = ''
                keyFlag = False
            if flag and not keyFlag:
                pair[key] = pair[key] + " " + word

    return pair

def processing_pair(pair, kabupaten):
    new_pair = {}
    for string in pair.keys():
        if string == 'kewarganegaraan' or string == 'agama' or string == 'hingga' or string == 'perkawinan':
            temp = pair[string].split(' ')
            temp = temp[2:3]
            new_pair[string] = ' '.join(temp)
        elif string == 'tempattgl':
            temp = pair[string].split(' ')
            temp = temp[2:]
            new_pair[string] = ' '.join(temp)
            new_pair[string] = new_pair[string].replace('lahir ', '')
        elif string == 'pekerjaan':
            temp = pair[string].split(' ')
            temp = temp[2:]
            # temp = ' '.join(temp)
            i = 0
            new_temp = []
            for t in temp:
                if i == len(temp)-1:
                    break
                flag = False
                for d in t:
                    if d.isdigit():
                        flag = True
                        break
                if flag:
                    i = i+1
                    if i == len(temp)-1: 
                        break
                else:
                    new_temp.append(t)
                    i = i+1
                    if i == len(temp)-1: 
                        break
            new_pair[string] = ' '.join(new_temp)
        else:
            temp = pair[string].split(' ')
            temp = temp[2:]
            new_pair[string] = ' '.join(temp)
    new_pair['kabupaten'] = kabupaten

    return new_pair

def get_blood_type(new_pair):
    darah = new_pair['kelamin'].split(' ')

    new_pair['kelamin'] = darah[0]
    new_pair['darah'] = darah[-1]

    return new_pair


# Convert to JSON
def pair_to_JSON(new_pair):
    list_key = new_pair.keys()
  
    new_dict = {}

    if 'provinsi' in list_key:
        new_dict['province'] = new_pair['provinsi']

    if 'kabupaten' in list_key:
        new_dict['district'] = new_pair['kabupaten']

    if 'nik' in list_key:
        new_dict['id_number'] = new_pair['nik']

    if 'nama' in list_key:
        new_dict['name'] = new_pair['nama']

    if 'tempattgl' in list_key:
        new_dict['place_date_of_birth'] = new_pair['tempattgl']

    if 'kelamin' in list_key:
        new_dict['gender'] = new_pair['kelamin']

    if 'darah' in list_key:
        new_dict['blood_type'] = new_pair['darah']

    if 'keldesa' in list_key:
        new_dict['address'] = new_pair['keldesa']

    if 'rtrw' in list_key:
        new_dict['neighborhood'] = new_pair['rtrw']

    if 'keldesa' in list_key:
        new_dict['village'] = new_pair['keldesa']

    if 'kecamatan' in list_key:
        new_dict['subdistrict'] = new_pair['kecamatan']

    if 'agama' in list_key:
        new_dict['religion'] = new_pair['agama']

    if 'perkawinan' in list_key:
        new_dict['marital_status'] = new_pair['perkawinan']

    if 'pekerjaan' in list_key:
        new_dict['occupation'] = new_pair['pekerjaan']

    if 'kewarganegaraan' in list_key:
        new_dict['nationality'] = new_pair['kewarganegaraan']

    if 'hingga' in list_key:
        new_dict['expiry_date'] = new_pair['hingga']

    res = {}

    for key in new_dict.keys():
        res[key] = new_dict[key].upper()

    json_object = json.dumps(res, indent = 4)

    return json_object