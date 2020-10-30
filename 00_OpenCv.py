import cv2
img = cv2.imread("Elephant.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow('GGWP',img)
cv2.waitKey(0)
cv2.destroyWindow()
