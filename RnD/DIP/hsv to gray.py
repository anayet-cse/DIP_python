
import skimage.io as io
from skimage.color import rgb2gray
from skimage.color import convert_colorspace
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import cv2

hsv= cv2.imread('D:\\DIP_python\\misc\\4.2.07.tiff', cv2.COLOR_RGB2HSV)

(h,s,v) = cv2.split(hsv)
v[:] = 100
img = cv2.merge((v, v, s))
rgb = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)	
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

grayf=ndi.uniform_filter(gray,3)
hb=3*gray-2*grayf

cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("high boost img", hb)
