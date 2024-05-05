from pytube import YouTube
import os


video_url = YouTube("https://www.youtube.com/watch?v=EGI-HL1WW7E&list=RDEGI-HL1WW7E&start_radio=1")

#get the audio from video file
mp4_no_video = video_url.streams.filter(only_audio=True).first()
outfile = mp4_no_video.download(output_path = "output_path")

##save the file

base, ext = os.path.splitext(outfile)
mp3_v = base + '.mp3'

os.rename(outfile, mp3_v)
