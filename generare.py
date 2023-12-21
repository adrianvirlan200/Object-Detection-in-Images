import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
import matplotlib.image
import numpy as np
from PIL import Image as im
import cv2

# generare imagini
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
images = model.text_to_image("photo of one computer keyboard and one computer mouse, "
                             "realistic, "
                             "color crimson "
                             "all the keys and all the buttons are crimson, all the keyboard is visible", batch_size=3)

# salvare imagini
for i in range(len(images)):
    matplotlib.image.imsave('out' + str(i) + '.png', images[i])
