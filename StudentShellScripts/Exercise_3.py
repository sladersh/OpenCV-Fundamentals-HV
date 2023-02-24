import numpy as np
import cv2


def nothing(x):
    pass


# named window for horizontal image stack
cv2.namedWindow("Horizontal_Stack_Trackbar", cv2.WINDOW_AUTOSIZE)

# named window for vertical image stack
cv2.namedWindow("Vertical_Stack_Trackbar", cv2.WINDOW_AUTOSIZE)

#  track bar added to horizontal stack
cv2.createTrackbar("Lower_Limit", "Horizontal_Stack_Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper_Limit", "Horizontal_Stack_Trackbar", 0, 255, nothing)

while True:
    img = cv2.imread("Pictures/piece03.png")
    img = cv2.resize(img, (120, 120))
    img_copy = img.copy()

    # finding lower bound limit and upper bound limit
    lower_bound = cv2.getTrackbarPos("Lower_Limit", "Horizontal_Stack_Trackbar")
    upper_bound = cv2.getTrackbarPos("Upper_Limit", "Horizontal_Stack_Trackbar")

    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    # copy of original image using 5 different thresholds
    ret1, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    ret2, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    ret3, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    ret4, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
    ret5, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

    # combining images
    images = [thresh1, thresh2, thresh3, thresh4, thresh5]

    img_horizontal_stack = np.hstack(images)  # horizontal stack
    cv2.imshow("Original Horizontal Stack", img_horizontal_stack)

    img_vertical_stack = np.vstack(images)  # vertical stack
    cv2.imshow("Original Vertical Stack", img_vertical_stack)

    ret1, thresh1 = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_BINARY)
    ret2, thresh2 = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_BINARY_INV)
    ret3, thresh3 = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_TRUNC)
    ret4, thresh4 = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_TOZERO)
    ret5, thresh5 = cv2.threshold(gray, lower_bound, upper_bound, cv2.THRESH_TOZERO_INV)

    images = [thresh1, thresh2, thresh3, thresh4, thresh5]

    img_horizontal_stack = np.hstack(images)
    cv2.imshow("Horizontal_Stack_Trackbar", img_horizontal_stack)

    img_vertical_stack = np.vstack(images)
    cv2.imshow("Vertical_Stack_Trackbar", img_vertical_stack)

    """
        Track bar is added to horizontal stack and works on both horizontal and vertical stacks
    """

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()
