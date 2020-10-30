import cv2 as cv2

img = cv2.imread("Elephant.jpg",cv2.IMREAD_COLOR)
cv2.imshow('Image',img)
cv2.waitkey(0)
cv2.destroyAllWindows()