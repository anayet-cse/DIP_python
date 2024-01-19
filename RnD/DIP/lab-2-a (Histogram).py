import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

img = io.imread('D:\\DIP_python\\misc\\7.2.01.tiff')

plt.subplot(2,2,1)
plt.imshow(img)


plt.subplot(2,2,2)
f = plt.figure()
f.show(plt.hist(img.flatten(), bins=256))

plt.show()
