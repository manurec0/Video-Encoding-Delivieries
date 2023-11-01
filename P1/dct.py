import math
import scipy


class dct:
    # implement 2D DCT
    def dct2(a):
        return scipy.fft.dct(scipy.fft.dct(a.T, norm='ortho').T, norm='ortho')

    # implement 2D IDCT
    def idct2(a):
        return scipy.fft.idct(scipy.fft.idct(a.T, norm='ortho').T, norm='ortho')

    from skimage.io import imread
    from skimage.color import rgb2gray
    import numpy as np
    import matplotlib.pylab as plt

# read RGB image and convert to grayscale
# im = rgb2gray(imread('input.jpeg'))
# imF = dct2(im)
# im1 = idct2(imF)
# im1 = imF

# np.allclose(im, im1)

# plt.gray()
# plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('original', size=20)
# plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('DCT+IDCT', size=20)
# plt.show()
