import skimage.io as io
from skimage.color import convert_colorspace

img = io.imread('D:\\DIP_python\\misc\\4.2.07.tiff')

img_hsv = convert_colorspace(img, 'RGB','HSV')

io.imshow(img_hsv)

io.show()

