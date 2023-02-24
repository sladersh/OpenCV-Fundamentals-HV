import numpy as np
from math import atan2, cos, sin, sqrt, pi
import cv2


def calculate_orientation(pts, img):
    size = len(pts)
    data_pts = np.empty((size, 2), dtype=np.float64)

    for i in range(data_pts.shape[0]):
        data_pts[i, 0] = pts[i, 0, 0]
        data_pts[i, 1] = pts[i, 0, 1]

    mean = np.empty((0))
    mean, eigenvectors, eigenvalues = cv2.PCACompute2(data_pts, mean)
    contour = (int(mean[0, 0]), int(mean[0, 1]))
    cv2.circle(img, contour, 3, (0, 255, 255), 2)
    p1 = (
        contour[0] + 0.02 * eigenvectors[0, 0] * eigenvalues[0, 0],
        contour[1] + 0.02 * eigenvectors[0, 1] * eigenvalues[0, 0],
    )
    p2 = (
        contour[0] - 0.02 * eigenvectors[1, 0] * eigenvalues[1, 0],
        contour[1] - 0.02 * eigenvectors[1, 1] * eigenvalues[1, 0],
    )
    draw_axes(img, contour, p1, (0, 0, 255), 1)
    draw_axes(img, contour, p2, (255, 0, 255), 5)

    # orientation in radians
    angle = atan2(eigenvectors[0, 1], eigenvectors[0, 0])
    return angle * 180 / pi  # converting to degree


def draw_axes(img, p, q, colour, scale):
    p1 = list(p)
    q1 = list(q)
    angle = atan2(p1[1] - q1[1], p1[0] - q1[0])  # angle in radians
    hypotenuse = sqrt(
        (p1[1] - q1[1]) * (p1[1] - q1[1]) + (p1[0] - q1[0]) * (p1[0] - q1[0])
    )
    # lengthening the arrow by a factor of scale
    q1[0] = p1[0] - scale * hypotenuse * cos(angle)
    q1[1] = p1[1] - scale * hypotenuse * sin(angle)
    cv2.line(
        img, (int(p1[0]), int(p1[1])), (int(q1[0]), int(q1[1])), colour, 1, cv2.LINE_AA
    )
    # create the arrow hooks
    p1[0] = q1[0] + 9 * cos(angle + pi / 4)
    p1[1] = q1[1] + 9 * sin(angle + pi / 4)
    cv2.line(
        img, (int(p1[0]), int(p1[1])), (int(q1[0]), int(q1[1])), colour, 1, cv2.LINE_AA
    )
    p1[0] = q1[0] + 9 * cos(angle - pi / 4)
    p1[1] = q1[1] + 9 * sin(angle - pi / 4)
    cv2.line(
        img, (int(p1[0]), int(p1[1])), (int(q1[0]), int(q1[1])), colour, 1, cv2.LINE_AA
    )


image = cv2.imread("Pictures/piece03.png")
image = cv2.resize(image, (960, 540))

# convert to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
dilation = cv2.dilate(blur, (9, 9), iterations=1)
ret, thresh = cv2.threshold(dilation, 120, 255, cv2.THRESH_BINARY_INV)

# finding contours
contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# finding centre and marking the center in the image
centre = []
for i in contours:
    M = cv2.moments(i)
    if M["m00"] != 0:
        centre_x = int(M["m10"] / M["m00"])
        centre_y = int(M["m01"] / M["m00"])

        centre.append((centre_x, centre_y))

for j in range(len(centre)):
    print(f"Centre of object {j + 1} = {centre[j]}")

orientation = []
for i, c in enumerate(contours):
    # find area of each contour
    area = cv2.contourArea(c)

    # ignore contours that are too large or too small
    if area < 1e2 or 1e5 < area:
        continue

    # drawing contours
    cv2.drawContours(image, contours, i, (0, 255, 0), 2)

    # find orientation
    orientation.append(calculate_orientation(c, image))

for j in range(len(orientation)):
    print(f"Orientation of object {j + 1} = {round(orientation[j], 2)} degrees")

cv2.imshow("Output Image", image)
cv2.waitKey(0)


"""
    O/P ->
        Centre of object 1 = (516, 399)
        Centre of object 2 = (157, 234)
        Centre of object 3 = (773, 213)
        Orientation of object 1 = 0.77 degrees
        Orientation of object 2 = 132.51 degrees
        Orientation of object 3 = 115.36 degrees
"""
