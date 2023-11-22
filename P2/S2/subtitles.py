import os

# Script for exercises 4 and 5


def download_subtitles(link):  # BROKEN!! most links have ad walls or are broken, so I just downloaded the subtitles
    # manually
    os.system("ffmpeg -i " + link + "-scodec srt BBB.srt")


def extract_embedded_subs(filename):  # Extract embedded subtitles from video file
    os.system("ffmpeg -i " + filename + " -map 0:s:0 " + filename[:-4] + ".srt")


def embed_subtitles(filename, subtitles):  # Embed subtitles file to video file
    os.system("ffmpeg -i " + filename + " -vf subtitles=" + subtitles + " " + filename[:-4] + "_srt.mp4")
