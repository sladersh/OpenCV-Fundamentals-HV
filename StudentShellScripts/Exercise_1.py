from PIL import Image
import cv2

##### Part 1

img1 = cv2.imread("Pictures/icons01.png")  # read icons01.png using OpenCV

dimensions = img1.shape  # shape returns (height in px, width in px, no. of channels)
img_type = img1.dtype  # return the type of the image

cv2.imshow("Showing icon01.png", img1)  # display icons01.png using OpenCV

print("Dimensions of icon01.png is", dimensions)
"""
    O/P -> Dimensions of icon01.png is (821, 2080, 3)
    
    The image has a height of 821 px, width of 2080 px and has 3 channels (R,G,B)
"""

print("Image type of icon01.png is", img_type)
"""
    O/P -> Image type of icon01.png is uint8

    uint8 means unsigned integer with 8 bits per channel (0 to 255)
"""

img11 = Image.open("Pictures/icons01.png")  # read icons01.png using PIL
img11.show()  # display icons01.png using PIL

print(f"Image file format of icons01.png is {img11.format}")
"""
    O/P -> Image file format of icons01.png is PNG
"""
print()

img2 = cv2.imread("Pictures/icons02.png")  # read icons02.png using OpenCV

dimensions = img2.shape
img_type = img2.dtype

cv2.imshow("Showing icon02.png", img2)  # display icons02.png using OpenCV

print("Dimensions of icon02.png is", dimensions)
"""
    O/P -> Dimensions of icon02.png is (821, 2080, 3)
"""

print("Image type of icon02.png is", img_type)
"""
    O/P -> Image type of icon02.png is uint8
"""

img22 = Image.open("Pictures/icons02.png")  # read icons02.png using PIL
img22.show()  # display icons01.png using PIL

print(f"Image file format of icons02.png is {img22.format}")
"""
    O/P -> Image file format of icons02.png is PNG
"""
print()

##### Part 2
img1 = cv2.imread("Pictures/rgb01.png")
img2 = cv2.imread("Pictures/rgb02.png")
img3 = cv2.imread("Pictures/rgb03.png")
cv2.imshow("rgb01.png", img1)
cv2.imshow("rgb02.png", img2)
cv2.imshow("rgb03.png", img3)

b1, g1, r1 = img1[99, 50]
b2, g2, r2 = img2[204, 116]
b3, g3, r3 = img3[45, 156]

print("BGR values of rgb01.png at (99, 50): ", b1, g1, r1)
print("BGR values of rgb02.png at (204, 116):", b2, g2, r2)
print("BGR values of rgb03.png at (45, 156):", b3, g3, r3)
"""
    O/P ->
        BGR values of rgb01.png at (99, 50):  255 183 183
        BGR values of rgb02.png at (204, 116): 255 0 0
        BGR values of rgb03.png at (45, 156): 0 0 255
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
