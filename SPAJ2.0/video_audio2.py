#final one
import moviepy.editor 
from tkinter.filedialog import *
# Function to convert video to audio
def video_to_audio(video_file, output_file):
    # Load the video file
    #video_clip = VideoFileClip(video_file)

    # Extract the audio from the video clip
    audio_clip = video_file.audio

    # Write the audio file
    audio_clip.write_audiofile(output_file)

# Example usage
vid = askopenfilename()
video_file = moviepy.editor.VideoFileClip(vid)   
#video_file = "input_video.mp4"
output_file = "output_audio3.mp3"
video_to_audio(video_file, output_file)
