from moviepy.video import VideoClip
import moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip
# from audio_extract import extract_audio
from assembly_accent import classify_accent
import os
import streamlit as st

## BACKEND
import requests
import uuid

from moviepy import VideoFileClip 
import os
import streamlit as st
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