# PDF to Audiobook

A simple Flask web application that allows users to upload a PDF file, extract the text, and convert it into an audiobook (MP3 format) using Google Cloud Text-to-Speech API.

## Features

- **Upload PDF**: Users can upload a PDF file to the web application.
- **Text Extraction**: The app extracts text from the uploaded PDF file using the PyMuPDF library.
- **Text-to-Speech**: The extracted text is converted into an MP3 audiobook using the Google Cloud Text-to-Speech API.
- **Audio Player**: Users can play the generated MP3 file directly on the website.
- **Download**: Users can download the generated audiobook in MP3 format.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Google Cloud Text-to-Speech API**: For converting text to speech.
- **PyMuPDF (fitz)**: For extracting text from PDF files.
- **HTML/CSS**: For creating the web interface.

## Requirements

1. Python 3.x
2. Google Cloud account and Text-to-Speech API enabled (API key required)
3. Flask
4. PyMuPDF
5. Google Cloud Python client (`google-cloud-texttospeech`)

## Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/zhudiana/pdf-audiobook-generator.git
cd pdf-audiobook-generator
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up Google Cloud API credentials:

- Go to your [Google Cloud Console](https://console.cloud.google.com/).
- Enable the Text-to-Speech API.
- Download the `service_account.json` file (credentials file).
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your `service_account.json`.

For example, on Linux/Mac:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service_account.json"
```

On Windows:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\service_account.json
```

### 4. Run the Flask application:

```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 5. Upload a PDF and generate an audiobook:

- Open the web application.
- Upload a PDF file.
- The text will be extracted and converted to speech.
- The MP3 file will be available for playback or download.

## Folder Structure

```
pdf-to-audiobook/
├── app.py                 # Flask app with routes and logic
├── requirements.txt       # List of Python dependencies
├── static/
│   └── audiobooks/        # Generated MP3 files
├── templates/
│   ├── upload.html        # HTML template for uploading PDFs
│   └── player.html        # HTML template for playing and downloading MP3
└── .gitignore             # To ignore sensitive files (e.g., service_account.json)
```

## Notes

- Remember to never push sensitive files like `service_account.json` to GitHub. Add them to `.gitignore` to prevent accidental commits.
- The `service_account.json` file is required for authenticating with the Google Cloud Text-to-Speech API.

---

Feel free to contribute or create issues if you encounter any bugs or have suggestions!

