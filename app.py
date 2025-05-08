import os
import fitz  # PyMuPDF
from google.cloud import texttospeech

from flask import Flask, render_template, request

app = Flask(__name__)

# Set your Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"


# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# Convert text to speech
def text_to_speech(text, output_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text[:5000])  # limit to 5000 chars per request
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
    print(f"Audio saved to {output_file}")


# Handles file upload, extracts text, converts to MP3, redirects to player
@app.route("/", methods=["GET", "POST"])
def upload_pdf():
    if request.method == "POST":
        pdf_file = request.files.get("pdf_file")
        pdf_path = os.path.join("uploads", pdf_file.filename)
        pdf_file.save(pdf_path)

        # Extract text and convert it to speech
        text = extract_text_from_pdf(pdf_path)
        output_file = os.path.join("static", "audiobooks", pdf_file.filename.split('.')[0] + ".mp3")
        text_to_speech(text, output_file)

        return render_template("player.html", filename=pdf_file.filename.split('.')[0] + ".mp3")

    return render_template("upload.html")


@app.route("/play/<filename>")
def play_audio(filename):
    return render_template("player.html", filename=filename)


if "__main__" == __name__:
    app.run(debug=True)
