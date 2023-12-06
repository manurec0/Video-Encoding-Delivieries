import os
from ffmpeg_python import display_info, change_res

# script with code and methods corresponding to exercises 1 and 2

video = "BBB.mp4"  # load video at 1920x1080
resolutions = ["1920:1080", "1280:720", "854:480", "360:240", "160:120"]

# from the first practice I have a method to change a given video's resolution, it will create another file with the new
# resolution. We can convert the video to various formats with this function:

change_res(video, resolutions[1])
change_res(video, resolutions[2])
change_res(video, resolutions[3])
change_res(video, resolutions[4])


class encoder:

    def __init__(self, filename):
        self.filename = filename
        self.name = filename[:-4]
        self.extension = filename[-4:]

    def vp8_encoder(self):
        os.system("ffmpeg -i " + self.filename + " -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis " + self.name +
                  "_VP8.webm")

    def vp9_encoder(self):
        os.system("ffmpeg -i " + self.filename + " -c:v libvpx-vp9 -b:v 1M " + self.name + "_VP9.webm")

    def h265_encoder(self):
        os.system("ffmpeg -i " + self.filename + " -c:v libx265 -crf 30 " + self.name
                  + "_H265.mp4")

    def av1_encoder(self):
        os.system("ffmpeg -i " + self.filename + " -c:v libsvtav1 -crf 50 " + self.name + "_AV1.mkv")


BBB = encoder("BBB_480.mp4")  # Create the video object of my class in order to have access to all the methods. Note
# that im using a lower resolution video in order to keep encoding times lower, but it should work with all resolutions

BBB.vp8_encoder()
BBB.vp9_encoder()
BBB.av1_encoder()

# BBB = encoder(video)

# BBB.h265_encoder()
# BBB.vp8_encoder()


def overlay_videos(left, right):
    os.system("ffmpeg -i " + left + " -i " + right + " -filter_complex hstack " + left[:-4] + "_" + right[:-4] +
              "_comparison.mp4")


overlay_videos("BBB_480_VP8.webm", "BBB_480_VP9.webm")
overlay_videos("BBB_480_VP9.webm", "BBB_480_AV1.mkv")
overlay_videos("BBB_480_VP9.webm", "BBB_480.mp4")

# We can see how the VP9 is the one with more file size and although it is subtle, especially in this resolution we can
# see how it is the one that best conserves the quality of the original
