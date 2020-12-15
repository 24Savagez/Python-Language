import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('gradient.png')
# threshold
_, th1 = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

# show image
plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(2, 3, 2)
plt.imshow(th1)
plt.title("Binary")

plt.subplot(2, 3, 3)
plt.imshow(th2)
plt.title("Bi_inverse")

plt.subplot(2, 3, 4)
plt.imshow(th3)
plt.title("Trunc")

plt.subplot(2, 3, 5)
plt.imshow(th4)
plt.title("To_zero")

plt.subplot(2, 3, 6)
plt.imshow(th5)
plt.title("To_zero_inv")


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
