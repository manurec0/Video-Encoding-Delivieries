import math
import scipy


class dct:
    # implement 2D DCT
    def dct2(a):
        return scipy.fft.dct(scipy.fft.dct(a.T, norm='ortho').T, norm='ortho')

    # implement 2D IDCT
    def idct2(a):
        return scipy.fft.idct(scipy.fft.idct(a.T, norm='ortho').T, norm='ortho')
