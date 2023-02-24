import cv2
import numpy as np

# reading the image
color_stripe = "Pictures/colorStripe.png"
image = cv2.imread(color_stripe)
bw, gw, rw = cv2.split(image)

b = image.copy()
# setting green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

g = image.copy()
# setting blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# setting blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

# RGB - Blue
cv2.imshow("B-RGB", b)
cv2.imshow("BW B-RGB", bw)
# RGB - Green
cv2.imshow("G-RGB", g)
cv2.imshow("GW G-RGB", gw)
# RGB - Red
cv2.imshow("R-RGB", r)
cv2.imshow("RW R-RGB", rw)
cv2.waitKey(0)

"""
    img[:,:,0] corresponds to the blue channel, img[:,:,1] corresponds to the green channel and img[:,:,2] corresponds to the red channel
"""
