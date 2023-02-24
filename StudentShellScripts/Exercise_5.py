import numpy as np
import cv2


def nothing(x):
    pass


cv2.namedWindow("Trackbar_Window")

# trackbar for gaussian blur
cv2.createTrackbar("Gaussian1", "Trackbar_Window", 1, 99, nothing)
cv2.createTrackbar("Gaussian2", "Trackbar_Window", 1, 99, nothing)

# trackbar for canny
cv2.createTrackbar("Canny1", "Trackbar_Window", 0, 255, nothing)
cv2.createTrackbar("Canny2", "Trackbar_Window", 0, 255, nothing)

# trackbar for dilate
cv2.createTrackbar("Dilate1", "Trackbar_Window", 1, 99, nothing)
cv2.createTrackbar("Dilate2", "Trackbar_Window", 1, 99, nothing)


while True:
    img = cv2.imread("Pictures/piece05.png")
    img_original = img.copy()

    # getting trackbar values for gaussian blur, canny and dilation
    gauss1 = cv2.getTrackbarPos("Gaussian1", "Trackbar_Window")
    gauss2 = cv2.getTrackbarPos("Gaussian2", "Trackbar_Window")
    thresh1 = cv2.getTrackbarPos("Canny1", "Trackbar_Window")
    thresh2 = cv2.getTrackbarPos("Canny2", "Trackbar_Window")
    dilate1 = cv2.getTrackbarPos("Dilate1", "Trackbar_Window")
    dilate2 = cv2.getTrackbarPos("Dilate2", "Trackbar_Window")

    # adjusting gaussian blur value
    if gauss1 % 2 == 0:
        gauss1 += 1
    if gauss2 % 2 == 0:
        gauss2 += 1

    # performing gray scale, gaussian blur, canny and dilation operations
    gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    gauss_blurred = cv2.GaussianBlur(gray, (gauss1, gauss2), 0)
    canny = cv2.Canny(gauss_blurred, thresh1, thresh2, 3)
    dilated = cv2.dilate(canny, (dilate1, dilate2), iterations=2)

    # finding contours
    contours, hierarchy = cv2.findContours(
        dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    # modifying the image shapes to stack together
    gray = np.stack((gray,) * 3, axis=-1)
    gauss_blurred = np.stack((gauss_blurred,) * 3, axis=-1)
    canny = np.stack((canny,) * 3, axis=-1)
    dilated = np.stack((dilated,) * 3, axis=-1)

    images = [gray, gauss_blurred, canny, dilated]
    win_names = ["gray", "blurred", "edged", "dilated"]

    # stacking window horizontally
    img_stack = np.hstack(images)
    img_stack = cv2.resize(img_stack, (900, 300))

    cv2.imshow("Trackbar_Window", img_stack)

    print("Objects in the image:", len(contours))

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()

"""
    Objects in the image: 145
    Objects in the image: 145
    Objects in the image: 145
    Objects in the image: 70
    Objects in the image: 21252
    Objects in the image: 101
    Objects in the image: 121
"""
