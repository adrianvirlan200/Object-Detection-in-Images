import cv2
import numpy as np
import matplotlib.image
######################################################################################################################################
# 4

# path coorodonate
path = "yolov5-master\\runs\\detect\\exp\\labels\\generat1.txt"

# citesc si salvez in vectori coordonatele obiectelor
x = []
y = []
width  = []
height = []

with open(path) as file:
    for line in file: # read rest of lines
        data = line.split()
        x.append(float(data[1]))
        y.append(float(data[2]))
        width.append(float(data[3]))
        height.append(float(data[4]))

image = cv2.imread("generat1.png")

# coordonatele sunt normate
for i in range(len(x)):
    x[i] = x[i] * image.shape[0]
    y[i] = y[i] * image.shape[1]
    width[i] = width[i] * image.shape[0]
    height[i] = height[i] * image.shape[1]

obj = []
# decupaj_img = img[rand_start:rand_end, col_start:col_end]
for i in range(len(x)):
    obj.append(image[int(y[i] - height[i]/2):int(y[i] + height[i]/2), int(x[i] - width[i]/2):int(x[i] + width[i]/2)])

# salvare imagini
for i in range(len(obj)):
    cv2.imwrite("cropped_obj" + str(i) + ".png", obj[i])

######################################################################################################################################
# 5
img = cv2.imread("cropped_obj0.png", cv2.IMREAD_UNCHANGED)

# masca o aplic pe spatiul BGR
crimson_upper = np.array([90, 75, 255])
crimson_lower = np.array([30, 0, 70])

# creare masca
mask = cv2.inRange(img, crimson_lower, crimson_upper)

# aplicare masca
result = cv2.bitwise_and(img, img, mask=mask)

# convertire din bgr in hsl
# imagine cropata
#hsl_image = matplotlib.colors.rgb_to_hls(img)
hsl_image = cv2.cvtColor(result, cv2.COLOR_BGR2HLS)

# salvare masca si imagine mascata in spatiul BGR si HSL
cv2.imwrite("mask.png", mask)
cv2.imwrite("masked_image.png", result)
cv2.imwrite("hsl_image.png", hsl_image)

######################################################################################################################################
# 6

# transofrmarea imaginii mascate in imagine transparenta
tmp = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
b, g, r = cv2.split(result)
rgba = [b, g, r, alpha]
dst = cv2.merge(rgba, 4)
cv2.imwrite("masca_transparenta.png", dst)
