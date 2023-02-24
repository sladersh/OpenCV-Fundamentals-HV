import cv2
import numpy as np

image = cv2.imread("Pictures/star.png")
image = cv2.resize(image, (960, 540))  # resizing original image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)

# finding contours
contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# finding centre and marking the center in the image
for i in contours:
    M = cv2.moments(i)
    if M["m00"] != 0:
        centre_x = int(M["m10"] / M["m00"])
        centre_y = int(M["m01"] / M["m00"])
        cv2.drawContours(image, [i], -1, (0, 255, 0), 2)
        cv2.circle(image, (centre_x, centre_y), 7, (0, 255, 255), -1)
        cv2.putText(
            image,
            "center",
            (centre_x - 20, centre_y - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 0),
            2,
        )
    print(f"Centre is (x, y) = ({centre_x}, {centre_y})")
    """
        O/P -> Centre is (x, y) = (257, 320)
    """

cv2.imshow("Img", image)
cv2.waitKey(0)
