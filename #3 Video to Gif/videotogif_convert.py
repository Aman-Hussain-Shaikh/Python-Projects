#Video to Gif Convertor

from moviepy.editor import *

video = VideoFileClip("Tromeur_Gaulois.mp4").subclip(00,5).rotate(180)

video.write_gif("test_2.gif")