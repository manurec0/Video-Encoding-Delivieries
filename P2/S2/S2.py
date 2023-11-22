import os
from subtitles import embed_subtitles
import yuv




def trim_video(filename, start, end):
    os.system("ffmpeg -ss " + start + " -to " + end + " -i " + filename + " -c copy " + filename[:3] + "_trimmed.mp4")


def only_video(filename):
    os.system("ffmpeg -i " + filename + " -vcodec copy -an " + filename[:3] + "_silence.mp4")


def extract_audio(filename, channels, bitrate, codec):
    if channels == 1:
        os.system("ffmpeg -i " + filename + " -ac " + str(channels) + " -b:a " + bitrate + " -map a " + filename[:3] +
                  "_mono." + codec)
    else:
        os.system("ffmpeg -i " + filename + " -ac " + str(channels) + " -b:a " + bitrate + " -map a " + filename[:3] +
                  "_stereo." + codec)


def join_av_streams():
    os.system("ffmpeg -i BBB_silence.mp4 -i BBB_mono.mp3 -i BBB_stereo.mp3 -i BBB_mono.aac -map 0:v -map 1:a -map 2:a "
              "-map 3:a -c copy output.mp4")


def stream_info(filename):
    os.system("ffprobe -i " + filename)


class macroBlocks_motionVectors:

    def __init__(self, filename):
        self.filename = filename

    def debug_vector_macroblocks(self):
        os.system("ffmpeg -flags2 +export_mvs -i " + self.filename + " -vf codecview=mv=pf+bf+bb " + self.filename[:-4] +
                  "_debug.mp4")


# some parameters to start
video = "BBB.mp4"

start = "00:00:00"
end = "00:00:09"

# EXERCISE 1
trim_video(video, start, end)  # trim 9 seconds video
debug_video = macroBlocks_motionVectors("BBB_trimmed.mp4")  # create class object to debug trimmed video
debug_video.debug_vector_macroblocks()  # create a new video that shows macroblocks and vectors with the use of the
# class

# EXERCISE 2
trim_video(video, "00:00:00", "00:00:50")  # 50 seconds BBB
only_video("BBB_trimmed.mp4")  # 50 seconds only video
extract_audio("BBB_trimmed.mp4", 1, "124k", "mp3")  # 50 seconds only mono audio mp3
extract_audio("BBB_trimmed.mp4", 2, "64k", "mp3")  # 50 seconds only stereo audio with
# lower bitrate mp3
extract_audio("BBB_trimmed.mp4", 1, "124k", "aac")  # 50 seconds only mono audio aac
join_av_streams()  # join 50 seconds trimmed video with the different audio streams

# EXERCISE 3
stream_info("output.mp4")  # Display file info where we can see the different audio/video streams

# EXERCISES 4 AND 5
embed_subtitles(video, "BBB.srt")  # Embeds the downloaded subtitles into a mp4 file

# EXERCISE 6
yuv.overlay_histogram(video)
