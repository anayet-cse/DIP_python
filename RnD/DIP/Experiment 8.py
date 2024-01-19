#!/usr/bin/env python
# coding: utf-8

# # Morphological Operation
# 
# ### Dilation


import numpy as np
from skimage.morphology import binary_dilation as bwdilate
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt
import skimage.io as io


c = data.binary_blobs()
#c = data.horse()
sel = np.ones((3,3))
#sel = np.array([[0,1,0],[1,1,1],[0,1,0]])
c_01 = bwdilate(c,sel)


io.imshow(c)
io.show()

io.imshow(c_01)
io.show


# ### Erosion


from skimage.morphology import binary_erosion as bwerode

c_01 = bwerode(c,sel)



io.imshow(c)
io.show()

io.imshow(c_01)
io.show


# ### Binary Opening Closing


from skimage.morphology import closing, opening, binary_closing as bwclose, binary_opening as bwopen

test_open = bwopen(c,sel)

test_close = bwclose(c,sel)


io.imshow(test_open)
io.show()

io.imshow(test_close)
io.show


# ## Graycale



import skimage.morphology as mo

c = data.camera()

str = mo.square(5)

cd = mo.dilation(c,str)

ce = mo.erosion(c,str)

io.imshow(cd)
io.show()

io.imshow(ce)
io.show()





