# script to load the movie (or any mp4 video) and create an .mp2 file, change the resolution, change chrominance
# subsampling and displaying video information using ffmpeg

import os
import dct

video = "BBB.mp4"  # SELECT MP4 VIDEO
resolution = "1280:720"  # INPUT DESIRED RESOLUTION IN FORMAT xxxx:xxx
chroma = "yuv422p"  # INPUT CHROMINANCE IN FORMAT yuvXXXp


def mp4_to_mp2(filename):  # method to convert mp4 to mp2
    os.system("ffmpeg -i " + filename + " -c:v mpeg2video -q:v 5 -c:a mp2 -f vob BBB.mpg")


def change_res(filename, res):  # method to change mp4 to a given resolution
    os.system("ffmpeg -i " + filename + " -vf scale=" + res + " BBB_" + res[-3:] + ".mp4")


def chroma_subsampling(filename, yuv):  # method to change chroma subsampling of mp4
    os.system("ffmpeg -i " + filename + " -pix_fmt " + yuv + " BBB_" + yuv + ".mp4")


def display_info(filename):
    os.system("ffprobe -i BBB.mp4")


mp4_to_mp2(video)
change_res(video, resolution)
chroma_subsampling(video, chroma)
display_info(video)
