import skimage.io as io
from skimage.color import rgb2gray

img = io.imread('D:\\DIP_python\\misc\\4.2.07.tiff')

img_gray = rgb2gray(img)

io.imshow(img_gray)

io.show()

