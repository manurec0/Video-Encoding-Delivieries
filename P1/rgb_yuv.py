import sys
import os


# This script contains the methods and code corresponding to exercises 1 and 2.
# 1: Convert a given set of RGB values to YUV and then give the RGB conversion again using the formulas available in the
# lecture slides.
# 2: Resize a given image into lower resolution using ffmpeg.

def rgb2yuv(r, g, b):  # convert RGB values to YUV
    print("RGB: ", r, g, b)
    Y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    U = -0.148 * r - 0.291 * g + 0.439 * b + 128
    V = 0.439 * r - 0.368 * g - 0.071 * b + 128
    return Y, U, V


def yuv2rgb(y, u, v):  # convert YUV values to RGB
    B = 1.164 * (y - 16) + 2.018 * (u - 128)
    G = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.319 * (u - 128)
    R = 1.164 * (y - 16) + 1.596 * (v - 128)
    return R, G, B


def ffmpeg_resize(filename):
    os.system("ffmpeg -i " + filename + " -vf scale=320:240 output_resized.jpeg")


########################################################################################################################
# ENTER VALUES HERE
r = 50
g = 61
b = 70

# Or enter values by command line:

# r = int(input("Enter R value: "))
# g = int(input("Enter G value: "))
# b = int(input("Enter B value: "))


y, u, v = rgb2yuv(r, g, b)  # returns RGB values in YUV
print("Your RGB values converted to YUV are:", int(y), int(u), int(v))
r, g, b = yuv2rgb(y, u, v)
print("The YUV values converted back to RGB are: ", int(r), int(g), int(b))  # Converts YUV values back to RGB and
# prints it

########################################################################################################################
# ENTER IMAGE TO RESIZE
filename = "input.jpeg"

ffmpeg_resize(filename)
