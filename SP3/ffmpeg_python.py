import os

# script with methods from previous labs


def mp4_to_mp2(filename):  # method to convert mp4 to mp2
    os.system("ffmpeg -i " + filename + " -c:v mpeg2video -q:v 5 -c:a mp2 -f vob BBB.mpg")


def change_res(filename, res):  # method to change mp4 to a given resolution
    os.system("ffmpeg -i " + filename + " -vf scale=" + res + " BBB_" + res[-3:] + ".mp4")


def chroma_subsampling(filename, yuv):  # method to change chroma subsampling of mp4
    os.system("ffmpeg -i " + filename + " -pix_fmt " + yuv + " BBB_" + yuv + ".mp4")


def display_info(filename):
    os.system("ffprobe -i BBB.mp4")
