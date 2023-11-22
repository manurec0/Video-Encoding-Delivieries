import os
# Script for the extraction of YUV histograms, corresponding to exercise 6


def extract_histogram(filename):  # extracts ONLY the histogram and creates a new video
    os.system("ffmpeg -i " + filename + " -vf histogram " + filename[:3] + "_hist.mp4")


def overlay_histogram(filename):  # extracts the histogram and overlays it to the original video
    os.system("ffmpeg -i " + filename + " -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay " +
              filename[:3] + "_histogram_video.mp4")
