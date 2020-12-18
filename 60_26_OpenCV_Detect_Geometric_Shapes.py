import cv2
import numpy as np

image = cv2.imread("shapes.jpg")
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
