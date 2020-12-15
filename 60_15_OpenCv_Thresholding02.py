import cv2
import numpy as np

image = cv2.imread('sudoku.png', 0)
_, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Image", image)
#cv2.imshow("Binary", th1)
cv2.imshow("Mean_c", th2)
cv2.imshow("Gaussian_c", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
