import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

f = io.imread('E:\\Education\\4-1 all (Munny)\\DIP LAB\\DIP_LAB\DIP_LAB\\misc\\7.1.07.tiff')

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Double thresholded image')
plt.imshow(ex.rescale_intensity(((f>40)&(f<80)),out_range=(0.0,1.0)),cmap='gray')

plt.show()
