from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


# read image
# img = Image.open("Irene.jpg").convert("L")
# print(img.format,img.size,img.mode)
# img.show()


# mix RGB
# r,g,b = img.split()
# img = Image.merge("RGB",(g,b,r))

# Color transforms

img1 = Image.open("lena.jpg").convert("1")
img2 = Image.open("lena.jpg").convert("L")
img3 = Image.open("lena.jpg").convert("P")
img4 = Image.open("lena.jpg").convert("RGB")
img5 = Image.open("lena.jpg").convert("RGBA")
img6 = Image.open("lena.jpg").convert("CMYK")
img7 = Image.open("lena.jpg").convert("YCbCr")
img8 = Image.open("lena.jpg").convert("LA")
img9 = Image.open("lena.jpg").convert("HSV")
img10 = Image.open("lena.jpg").convert("I")
img11 = Image.open("lena.jpg").convert("F")

plt.figure(figsize=(10, 10))

plt.subplot(3, 4, 1)
plt.imshow(img1)
plt.title("1")

plt.subplot(3, 4, 2)
plt.imshow(img2)
plt.title("L")

plt.subplot(3, 4, 3)
plt.imshow(img3)
plt.title("P")

plt.subplot(3, 4, 4)
plt.imshow(img4)
plt.title("RGB")

plt.subplot(3, 4, 5)
plt.imshow(img5)
plt.title("RGBA")

plt.subplot(3, 4, 6)
plt.imshow(img6)
plt.title("CMYK")

plt.subplot(3, 4, 7)
plt.imshow(img7)
plt.title("YCbCr")

plt.subplot(3, 4, 8)
plt.imshow(img8)
plt.title("LA")

plt.subplot(3, 4, 9)
plt.imshow(img9)
plt.title("HSV")

plt.subplot(3, 4, 10)
plt.imshow(img10)
plt.title("I")

plt.subplot(3, 4, 11)
plt.imshow(img11)
plt.title("F")

plt.show()
