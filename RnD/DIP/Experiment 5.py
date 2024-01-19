#!/usr/bin/env python
# coding: utf-8

# # Fourier Transform of Image
# 
# ### Grayscale Image

# In[11]:


import numpy as np
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt

c = data.camera()

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Grayscal image')
plt.imshow(c, cmap='gray')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('DFT of the image')
plt.imshow(ex.rescale_intensity(cfsl,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# ### RGB image

# In[12]:


c = data.coffee()

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

plt.subplot(1,2,1)
plt.axis('off')
plt.title('RGB image')
plt.imshow(c, cmap='gray')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('DFT of the image')
plt.imshow(ex.rescale_intensity(cfsl,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# ### Index Image

# In[13]:


c = data.cell()

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Index image')
plt.imshow(c, cmap='gray')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('DFT of the image')
plt.imshow(ex.rescale_intensity(cfsl,out_range=(0.0,1.0)),cmap='gray')

plt.show()


# In[ ]:




