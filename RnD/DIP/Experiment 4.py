#!/usr/bin/env python
# coding: utf-8

# # Experimenting with image geometry

# ## Image Interpolation



import skimage.io as io
import skimage.transform as tr
import skimage.restoration as re
import skimage.data as data
import matplotlib.pyplot as plt

c = data.camera()

head = c[60:210, 150:300]

plt.figure()

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Head')
plt.imshow(head, cmap='gray')



head4a = tr.rescale(head,2,order=0)
plt.subplot(2,2,2)
plt.axis('off')
plt.title('Nearest')
plt.imshow(head4a,cmap='gray')



head4b = tr.rescale(head,2,order=1)
plt.subplot(2,2,3)
plt.axis('off')
plt.title('Bilinear')
plt.imshow(head4b,cmap='gray')


head4c = tr.rescale(head,2,order=3)
plt.subplot(2,2,4)
plt.axis('off')
plt.title('Bicubic')
plt.imshow(head4c,cmap='gray')


plt.show()




# ## Rotation
# 
# ### Anti Clockwise


crc = tr.rotate(c,60,order=3)

io.imshow(crc)
io.show()



# ### Clockwise


crc = tr.rotate(c,-60,order=1)

io.imshow(crc)
io.show()




# ## Image Enlarging


h = tr.rescale(head,4,order=3)

io.imshow(h)
io.show()




# ## Image Subsampling


h = tr.rescale(head,0.25,order=3) # >9.0

io.imshow(h)
io.show()






############################################################################



# ### Unnecessary (Enlargement by spatial filtering)
# ### Note complete



import numpy as np
import scipy.ndimage as ndi

m = np.array([[16,2,2,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]])

r,c = m.shape

m2 = np.zeros((2*r,2*c))

m2[::2,::2] = m2

# Applying Filter


x = ndi.convolve(m2,np.array([[0,0,0],[0,1,1],[0,1,0]]),mode='constant')

y = ndi.convolve(m2,np.array([[1,2,1],[2,4,2],[1,2,1]])/4.0,mode='constant')





# In[ ]:




