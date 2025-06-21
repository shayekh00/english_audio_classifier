# 🦜🔗  English Accent Classifier

This project is a Streamlit-based web app that takes a video URL (from Loom or direct MP4 link), extracts audio, and classifies the English accent using AssemblyAI's API.

# 🚀 Features

Upload Loom or direct MP4 URLs

Extracts audio automatically

Sends audio to AssemblyAI for transcription and language detection

Returns accent (inferred from language code), confidence score, and transcript preview

# 🗂️ Project Structure
project-root/

├── frontend.py                  # Main Streamlit UI

├── audio_extract.py             # Audio extraction logic

├── assembly_accent.py          # Accent classification via AssemblyAI

├── loomdl.py                   # Loom video downloader logic

├── extracted_video/            # Folder to store downloaded videos

├── extracted_audio/            # Folder to store extracted audio

├── .env                        # Environment variables (NOT committed)

├── .gitignore

├── requirements.txt            # Python dependencies

└── .streamlit/
    └── secrets.toml            # Secrets for Streamlit Cloud

    
🔧 Setup Instructions

1. Clone the repo

git clone https://github.com/your-username/english-accent-classifier.git
cd english-accent-classifier

2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Create a .env file

Create a .env file in the root folder:


ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here

5. Run the app

streamlit run frontend.py

🌐 Deployment (Streamlit Cloud)

Upload your code to GitHub

Go to streamlit.io/cloud and create a new app

Add your secrets in secrets.toml via the Streamlit UI:

OPENAI_API_KEY = "sk-..."
ASSEMBLYAI_API_KEY = "your_assemblyai_api_key"

Deploy and share!

🧪 Test Video URL

Use this sample MP4 URL for testing:

https://filesamples.com/samples/video/mp4/sample_640x360.mp4

✅ Requirements

See requirements.txt for a full list. Includes:

streamlit

moviepy

openai

langchain

requests

python-dotenv

beautifulsoup4

lxml

imageio-ffmpeg