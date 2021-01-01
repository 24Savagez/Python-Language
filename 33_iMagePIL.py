from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# read image
image1 = Image.open("Irene.jpg").convert("L")
image2 = Image.open("Seulki.jpg")

# display image
plt.imshow(image1)
plt.imshow(image2)
image1.show()
# image2.show()

# show image properties
print("im1 :", image2.size)  # Width x height
print("im1 :", image2.format)
print("im1 :", image2.mode)

# save as image
image1.save("Irene02.JPG")

# crop image
left = 160
top = 50
right = 460
bottom = 430

cropped_image = image1.crop((left, top, right, bottom))
plt.imshow(cropped_image)
# cropped_image.show()

# copy imange
copied_image = image2.copy()
plt.imshow(copied_image)
# copied_image.show()

# Transposting
transposed_im1 = image2.transpose(Image.FLIP_LEFT_RIGHT)
transposed_im2 = image2.transpose(Image.FLIP_TOP_BOTTOM)
transposed_im3 = image2.transpose(Image.ROTATE_90)
transposed_im4 = image2.transpose(Image.ROTATE_180)
transposed_im5 = image2.transpose(Image.ROTATE_270)
transposed_im6 = image2.transpose(Image.TRANSPOSE)

plt.figure(figsize=(10, 10))

# fill image for 1 picture
plt.subplot(2, 3, 1)
plt.imshow(transposed_im1)
plt.title("Flip left to right")

plt.subplot(2, 3, 2)
plt.imshow(transposed_im2)
plt.title("Flip top to bottom")

plt.subplot(2, 3, 3)
plt.imshow(transposed_im3)
plt.title("Rotate 90 degree")

plt.subplot(2, 3, 4)
plt.imshow(transposed_im4)
plt.title("Rotate 180 degree")

plt.subplot(2, 3, 5)
plt.imshow(transposed_im5)
plt.title("Rotate 270 degree")

plt.subplot(2, 3, 6)
plt.imshow(transposed_im6)
plt.title("Transpose")

# plt.show()

# rotating
plt.figure(3)
angle = 30
rotated_im = image2.rotate(angle)
plt.imshow(rotated_im)
# plt.show()
