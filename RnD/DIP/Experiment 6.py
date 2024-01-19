#!/usr/bin/env python
# coding: utf-8

# # Adding and removing noises from images (grayscale)
# 

# In[47]:


import numpy as np
import skimage.data as data
import skimage.io as io
import skimage.util.noise as noise
import scipy.ndimage as ndi


img = data.camera()
io.imshow(img)
io.show()



# ## Salt & Pepper Noise

# In[53]:


xn = noise.random_noise(img,mode='s&p',amount=0.005)
io.imshow(xn)
io.show()


# ### Removing Salt & Pepper
# 
# #### Low pass filtering - Uniform Filter
# 

# In[49]:


uni_xn = ndi.uniform_filter(xn,7)
io.imshow(uni_xn)
io.show()


# #### Median Filter

# In[50]:


med_xn=ndi.median_filter(xn,3) 
io.imshow(med_xn)
io.show()


# #### Rank Order Method

# In[51]:


cross = np.array([[0,1,0],[1,1,1],[0,1,0]])
ran_xn = ndi.median_filter(nimg1,footprint=cross)
io.imshow(ran_xn)
io.show()


# #### Outlier Method

# In[52]:


av = np.array([[1,1,1],[1,0,1],[1,1,1]])/8.0
gspa = ndi.convolve(xn,av)
D = 0.5
r = (abs(xn-gspa)>D)*1.0
io.imshow(r*gspa+(1-r)*xn)
io.show()


# ## Gaussian Noise

# In[59]:


xg = noise.random_noise(img,'gaussian')
io.imshow(xg)
io.show()


# ### Removing Gaussian Noise
# 
# #### Image Averaging

# In[68]:


x,y = img.shape

t = np.zeros((x,y,100))

for i in range(100):
    t[:,:,i] = noise.random_noise(img,'gaussian')

ta = np.mean(t,2)
    
io.imshow(ta)
io.show()



# #### Using Average Filter

# In[63]:


f=np.ones((3,3))/9
img03= ndi.convolve(xg, f, mode='constant')
io.imshow(img03,cmap='gray')
io.show()


# #### Using Adaptive Filter

# In[73]:


from scipy.signal import wiener
import skimage.exposure as ex

cw1 = wiener(xg,[7,7])

io.imshow(ex.rescale_intensity(cw1,out_range=(0.0,1.0)),cmap='gray')
io.show()


# ## Periodic Noise
# 
# ### Removing
# 

# In[75]:


import numpy as np
import skimage.io as io
import skimage.exposure as ex
from skimage.util import img_as_float,img_as_ubyte
from numpy.fft import ifft2,fft2,fftshift
import math

g = io.imread('D:\\DIP_python\\Dataset\\misc\\7.1.05.tiff')
io.imshow(g)
io.show()

r,c=g.shape
x,y=np.mgrid[0:r,0:c].astype('float32')
p=np.sin(x/3+y/3)+1.0
gp=(2*img_as_float(g)+p/2)/3
io.imshow(gp)
io.show()

gf=fftshift(fft2(gp))
temp=ex.rescale_intensity(abs(gf), out_range=(0,1))
gf2=img_as_ubyte(temp)
gf2[200,200]=0
i,j=np.where(gf2==gf2.max())
c=np.sqrt((i-200)**2+(j-200)**2)
cf=fftshift(ifft2(c))


z=np.sqrt((x-200)**2+(y-200)**2)
k=1
d=math.sqrt(610.0)
br=(z<np.floor(d-k))|(z>np.ceil(d+k))
cfr=cf*br
io.imshow(cfr)
io.show()


# In[ ]:




