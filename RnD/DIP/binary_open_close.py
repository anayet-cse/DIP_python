import numpy as np
from skimage.morphology import binary_opening as bwopen,binary_closing as bwclose
import skimage.data as data
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

c = data.binary_blobs()
sel = np.ones((3,3))
test_open = bwopen(c,sel)
test_close = bwclose(c,sel)

io.imshow(c)
io.show()
io.imshow(test_open)
io.show()
io.imshow(test_close)
io.show()

