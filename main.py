from moviepy.video import VideoClip
import moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip
from audio_extract import extract_audio

video_path = "loom_downloaded_video.mp4"
audio_path = video_path.replace(".mp4", ".wav")

extract_audio(input_path=video_path, output_path=audio_path)

