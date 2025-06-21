from moviepy.video import VideoClip
import moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip
# from audio_extract import extract_audio
from assembly_accent import classify_accent
import ffmpeg
import os
import streamlit as st

## BACKEND
import requests
import uuid

from loomdl import download_loom_video, fetch_loom_download_url, extract_id
    
def download_video(video_url):
    filename = f"{uuid.uuid4()}.mp4"  # This saves to root dir (same as frontend.py)
    
    try:
        response = requests.get(video_url, stream=True)
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return filename
    except Exception as e:
        st.error(f"Failed to download video: {e}")
        return None




# def audio_extraction(video_path):
    
#     audio_path = video_path.replace(".mp4", ".mp3")
#     try:
#         st.write(f"Extracting audio from video")
#         audio_path = "extracted_audio/"+audio_path

#         extract_audio(input_path="./extracted_video/"+video_path, output_path=audio_path)


#         return audio_path
#     except Exception as e:
#         st.error(f"Audio extraction failed: {e}")
#         return None
    

# def audio_extraction(video_path):
#     audio_path = video_path.replace(".mp4", ".mp3")

#     # # Ensure output directories exist
#     # os.makedirs("./extracted_audio", exist_ok=True)
#     # os.makedirs("./extracted_video", exist_ok=True)

#     # final_input_path = os.path.join("extracted_video", video_path)
#     # final_output_path = os.path.join("extracted_audio", audio_path)

#     final_input_path = "0739fd5b-bab1-4637-909d-43552f36f9ba.mp4"
#     final_output_path = audio_path

#     try:
#         st.write(f"Extracting audio from video: {final_input_path}")
#         ffmpeg.input(final_input_path).output(final_output_path, acodec='mp3', vn=None).run(overwrite_output=True)
#         return final_output_path
#     except ffmpeg.Error as e:
#         raise RuntimeError(f"FFmpeg failed: {e.stderr.decode()}")


from moviepy import VideoFileClip 
import os
import streamlit as st

def audio_extraction(video_path):
    audio_filename = video_path.replace(".mp4", ".mp3")
    final_input_path = os.path.join("extracted_video", video_path)
    final_output_path = os.path.join("extracted_audio", audio_filename)

    # Ensure the output directory exists
    os.makedirs("extracted_audio", exist_ok=True)

    try:
        st.write(f"Extracting audio using moviepy from: {final_input_path}")
        video = VideoFileClip(final_input_path)
        video.audio.write_audiofile(final_output_path)
        return final_output_path
    except Exception as e:
        st.error(f"Audio extraction failed using moviepy: {e}")
        return None