import numpy as np
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

img01= io.imread('C:\\Users\\lab1\\Desktop\\Emon 27\\dip\\misc\\7.1.05.tiff')

io.imshow(img01)
io.show()

img02= ex.equalize_hist(img01)

io.imshow(img02)
io.show()

f = plt.figure()
f.show(plt.hist(img02.flatten(), bins=256))

plt.show()
