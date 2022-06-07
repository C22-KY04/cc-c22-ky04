import numpy as np
import tensorflow as ts

def image_classification():
    img = tf.keras.utils.load_img("tmp/image.png", target_size=(204, 324))
    img_array = tf.keras.utils.img_to_array(img)
    classes = load_model.predict(np.expand_dims(img_array, axis=0))

    if classes == 0:
        return True
    else:
        return False