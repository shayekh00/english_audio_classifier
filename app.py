from audio_extract import extract_audio
from assembly_accent import classify_accent
import uuid
import streamlit as st
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from backend_logic import download_video, audio_extraction, download_loom_video, fetch_loom_download_url, extract_id

st.set_page_config(page_title="🦜🔗 English Accent Classifier")
st.title('🦜🔗 English Accent Classifier')

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))




with st.form('my_form'):
  col1, col2, col3 = st.columns([1, 2, 1])  # Adjust width ratios as needed
  with col2:
    text = st.text_area('Enter Video URL ( You can use the given link as well ):',
                        "https://www.loom.com/share/fdea98eb5a5e4a7585b7e415f6b7db76?sid=7fef4af4-2a43-474e-87a2-9f05c805fc18",
                         placeholder='https://www.loom.com/share/fdea98eb5a5e4a7585b7e415f6b7db76?sid=7fef4af4-2a43-474e-87a2-9f05c805fc18', height=100)
    submitted = st.form_submit_button('Submit')
    

    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner("Processing..."):
            st.write(f"Processing video URL: {text}")
            if "loom.com" in text:
                id = extract_id(text)
                url = fetch_loom_download_url(id)
                filename = f"{uuid.uuid4()}.mp4"
                loom_filename = f"extracted_video/{filename}"
                download_loom_video(url, loom_filename)
                
                # video_path = download_loom_video(text)
            else:
                filename = download_video(text)

            if filename:
                
                audio_path = audio_extraction(filename)
                if audio_path:
                    st.write(f"Classifying accent from the audio...")
                    accent, confidence, explanation = classify_accent(audio_path)

                    st.success("✅ Analysis Complete")
                    st.metric(label="Detected Accent", value=accent)
                    st.metric(label="Confidence in English", value=f"{confidence}%")
                    st.info(explanation)