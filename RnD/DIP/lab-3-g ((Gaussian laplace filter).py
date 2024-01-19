import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img01= data.camera()
plt.subplot(1,2,1)
plt.imshow(img01)


img02= ndi.gaussian_laplace(img01,2)
plt.subplot(1,2,2)
plt.imshow(img02)
plt.show()
