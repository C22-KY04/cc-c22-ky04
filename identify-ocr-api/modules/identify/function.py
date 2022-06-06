# from google.cloud import storage
import numpy as np
import urllib.request
import cv2
import tensorflow as tf
import tensorflow.keras.preprocessing.image as tfimg
import matplotlib.pyplot as plt

# def download_model_file():

#   # Model Bucket details
#   BUCKET_NAME        = "YOUR_MODEL_BUCKET_NAME"
#   PROJECT_ID         = "YOUR_GCP_PROJECT_ID"
#   GCS_MODEL_FILE     = "MODEL_FILE_NAME.pkl"

#   # Initialise a client
#   client   = storage.Client(PROJECT_ID)
    
#   # Create a bucket object for our bucket
#   bucket   = client.get_bucket(BUCKET_NAME)
    
#   # Create a blob object from the filepath
#   blob     = bucket.blob(GCS_MODEL_FILE)
    
#   folder = '/tmp/'
#   if not os.path.exists(folder):
#   os.makedirs(folder)
#   # Download the file to a destination
#   blob.download_to_filename(folder + "model.h5")

model = tf.keras.models.load_model('model.h5')

def url_to_image(url):
  source_file = urllib.request.urlopen(url)
  image = np.asarray(bytearray(source_file.read()), dtype="uint8")
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image
  
def identify(image):
  img = tfimg.load_img(image, target_size = (204, 324))
  imgplot = plt.imshow(img)
  x = tfimg.img_to_array(img)
  x = np.expand_dims(x, axis = 0)

  images = np.vstack([x])
  classes = model.predict(images, batch_size = 10)

  if classes==0:
    return 'ktp'
  else:
    return 'nonktp'

def doidentify(url):
  img = url_to_image(url)
  return identify(img)