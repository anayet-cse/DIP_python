import skimage.morphology as mo
import skimage.data as data
import skimage.io as io
import numpy as np


c = data.camera()
str = mo.square(5)
cd = mo.dilation(c,str)
ce = mo.erosion(c,str)

io.imshow(c)
io.show()
io.imshow(cd)
io.show()
io.imshow(ce)
io.show()

