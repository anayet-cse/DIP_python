#!/usr/bin/env python
# coding: utf-8

# # Image Thresholding and Edge Detection
# 
# 
# ## Image Thresholding
# 
# ### Single Thresholding
# 
# 
# #### Single Thresholding using selected value



import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex
import skimage.filters as fl
import numpy as np

f = io.imread('D:\\DIP_python\\Dataset\\misc\\7.1.05.tiff')

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Single thresholded image')
plt.imshow(ex.rescale_intensity(f<50,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# #### Single Thresholding using Otsu method


plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

t = fl.threshold_otsu(f)

print(t)

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Single thresholded image')
plt.imshow(ex.rescale_intensity(f<t,out_range=(0.0,1.0)),cmap='gray')

plt.show()




plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

t = fl.threshold_isodata(f)

print(t)

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Single thresholded image')
plt.imshow(ex.rescale_intensity(f<t,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# ### Double Thresholding


plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Double thresholded image')
plt.imshow(ex.rescale_intensity(((f>40)&(f<80)),out_range=(0.0,1.0)),cmap='gray')

plt.show()


# ### Adaptive Thresholding



f = io.imread('D:\\DIP_python\\Dataset\\misc\\7.1.05.tiff')

r,c = f.shape

x,y = np.mgrid[0:r, 0:c]

p = 255 - f + y/2

io.imshow(ex.rescale_intensity(p,out_range=(0.0,1.0)),cmap='gray')
io.show()


# ## Edge Detection
# 
# ### Prewitt


import skimage.io as io
import skimage.filters as fl
import matplotlib.pyplot as plt
import skimage.exposure as ex
 
f = io.imread('D:\\DIP_python\\Dataset\\misc\\7.1.05.tiff')

edge_p=fl.prewitt(f)

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(ex.rescale_intensity(f,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Filtered image with Prewitt operator')
plt.imshow(ex.rescale_intensity(edge_p,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# ## Roberts
# 


edge_p=fl.roberts(f)

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(ex.rescale_intensity(f,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Filtered image with Prewitt operator')
plt.imshow(ex.rescale_intensity(edge_p,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# ### Sobel



edge_p=fl.sobel(f)

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(ex.rescale_intensity(f,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Filtered image with Prewitt operator')
plt.imshow(ex.rescale_intensity(edge_p,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# ### Laplacian



import skimage.util as ut

s = ut.img_as_float(f)

s_lap = abs(fl.laplace(s))

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(ex.rescale_intensity(f,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Filtered image with Laplacian filter')
plt.imshow(ex.rescale_intensity(s_lap,out_range=(0.0,1.0)),cmap='gray')

plt.show()





