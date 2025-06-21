from moviepy.video import VideoClip
import moviepy
from moviepy.video.io.VideoFileClip import VideoFileClip
from audio_extract import extract_audio
from assembly_accent import classify_accent

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




def audio_extraction(video_path):
    
    audio_path = video_path.replace(".mp4", ".mp3")
    try:
        st.write(f"Extracting audio from video")
        audio_path = "extracted_audio/"+audio_path

        extract_audio(input_path="./extracted_video/"+video_path, output_path=audio_path)


        return audio_path
    except Exception as e:
        st.error(f"Audio extraction failed: {e}")
        return None