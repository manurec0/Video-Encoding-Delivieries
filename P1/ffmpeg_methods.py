import os

# This script contains the methods for exercise 4. Converts a given image into grayscale


def ffmpeg_grayscale(filename):
    os.system("ffmpeg -i " + filename + " -vf format=gray output_grayscale.jpeg")


# ENTER IMAGE
filename = "input.jpeg"

ffmpeg_grayscale(filename)
