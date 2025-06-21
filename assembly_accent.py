# assembly_accent.py

import requests
import time
import os

BASE_URL = "https://api.assemblyai.com"
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
# print(f"Using AssemblyAI API Key: {ASSEMBLYAI_API_KEY}")
HEADERS = {"authorization": ASSEMBLYAI_API_KEY}


def upload_to_assemblyai(audio_path):
    with open(audio_path, "rb") as f:
        response = requests.post(
            f"{BASE_URL}/v2/upload",
            headers=HEADERS,
            data=f
        )
    response.raise_for_status()
    return response.json()["upload_url"]


def interpret_language_as_accent(lang_code):
    mapping = {
        "en_us": "American",
        "en_gb": "British",
        "en_au": "Australian",
        "en_in": "Indian",
        "en":    "English (General)"
    }
    return mapping.get(lang_code.lower(), "Unknown")


def classify_accent(audio_path):
    upload_url = upload_to_assemblyai(audio_path)

    transcript_request = {
        "audio_url": upload_url,
        "language_detection": True
    }

    response = requests.post(f"{BASE_URL}/v2/transcript", json=transcript_request, headers=HEADERS)
    response.raise_for_status()
    transcript_id = response.json()['id']
    polling_endpoint = f"{BASE_URL}/v2/transcript/{transcript_id}"

    while True:
        transcription_result = requests.get(polling_endpoint, headers=HEADERS).json()
        status = transcription_result['status']

        if status == 'completed':
            lang_code = transcription_result.get('language_code', 'unknown')
            confidence = transcription_result.get('language_confidence', 0)
            text = transcription_result.get('text', '')
            label = interpret_language_as_accent(lang_code)
            explanation = f"Detected language code: {lang_code}, interpreted as {label} accent.\n\nTranscript: {text[:200]}..."
            return label, round(confidence * 100, 2), explanation

        elif status == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        else:
            time.sleep(3)
