from PIL import Image
import cv2

x = 1676
y = 1046
flower_img = "Pictures/flower.png"
eagle_img = "Pictures/eagle.png"
car_img = "Pictures/car.png"


##### Part 1

img1 = cv2.imread(flower_img)
img11 = Image.open(flower_img)
img2 = cv2.imread(eagle_img)
img22 = Image.open(eagle_img)

dimensions1 = img1.shape  # dimension of flower.png
height1, width1, channel1 = (img1.shape[0], img1.shape[1], img1.shape[2])
type1 = img1.dtype  # data type of flower.png
resolution1 = img11.size  # resolution of flower.png
image_mode1 = img11.mode  # mode of flower.png

dimensions2 = img2.shape  # dimension of eagle.png
height2, width2, channel2 = (img2.shape[0], img2.shape[1], img2.shape[2])
type2 = img2.dtype  # data type of eagle.png
resolution2 = img22.size  # resolution of eagle.png
image_mode2 = img22.mode  # mode of eagle.png

print(f"For flower.png dimension = {dimensions1}")
print(f"For flower.png height = {height1}, width = {width1}, channels = {channel1}")
print(f"For flower.png type = {type1}")
print(f"For flower.png resolution = {resolution1}")
print(f"For flower.png image mode = {image_mode1}")
"""
    O/P ->
        For flower.png dimension = (1632, 1224, 3)
        For flower.png height = 1632, width = 1224, channels = 3
        For flower.png type = uint8
        For flower.png resolution = (1224, 1632)
        For flower.png image mode = L
        
    Mode L means 8-bit black and white pixels
"""
print()

print(f"For eagle.png dimension = {dimensions2}")
print(f"For eagle.png height = {height2}, width = {width2}, channels = {channel2}")
print(f"For eagle.png type = {type2}")
print(f"For eagle.png resolution = {resolution2}")
print(f"For eagle.png image mode = {image_mode2}")
"""
    O/P ->
        For eagle.png dimension = (667, 1000, 3)
        For eagle.png height = 667, width = 1000, channels = 3
        For eagle.png type = uint8
        For eagle.png resolution = (1000, 667)
        For eagle.png image mode = RGB
        
    Mode RGB means 3x8 bit pixels which are true color
"""
print()


##### Part 2

img3 = cv2.imread(car_img)
b1, g1, r1 = img3[x, y]
print(
    f"For car.png RGB values at (1676, 1046) are Blue = {b1}, Green = {g1}, Red = {r1}"
)
"""
    O/P -> For car.png RGB values at (1676, 1046) are Blue = 165, Green = 139, Red = 115
"""

cv2.destroyAllWindows()
