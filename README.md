Real-Time Speech-to-Speech Translation App
This repository contains a real-time speech-to-speech translation application built using Python, Flask, and various NLP libraries. The app listens to spoken language, translates it into a target language, and plays the translated speech back to the user. The application supports various translation services such as DeepL, Google Translate API, and local models.


Real-Time Speech Recognition: Converts spoken words into text using the Google Speech Recognition API.
Multiple Translation Options: Supports translation via DeepL, Google Translate API, or local NLP models.
Text-to-Speech Conversion: Converts translated text back into speech in the target language.
Real-Time Feedback: Displays the recognized speech and translated text on the web interface.
User-Friendly Interface: A simple web interface built with Flask and styled with CSS.
Demo

Installation
Prerequisites
Python 3.7+
pip (Python package installer)
Clone the Repository
bash
Copy code
git clone https://github.com/amitdeagarwal/Speech-to-Speech-realtime.git
cd Speech-to-Speech-realtime
Set Up Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Additional Dependencies
PyAudio: Required for capturing audio input.
On Linux: sudo apt-get install portaudio19-dev
On macOS: brew install portaudio
On Windows: Install using pipwin:
bash
Copy code
pip install pipwin
pipwin install pyaudio
Configuration
The app can be configured to use different translation services via environment variables.

Environment Variables
Create a .env file in the root directory of the project and add the following configurations:

bash
Copy code
# Translation Service (options: 'local', 'deepl', 'google')
TRANSLATION_SERVICE=local

# If using DeepL API
DEEPL_API_KEY=your_deepl_api_key

# If using Google Translate API
GOOGLE_API_KEY=your_google_api_key

# Target Language (e.g., 'de' for German)
TARGET_LANGUAGE=de
Usage
Running the App
Start the Flask app:

bash
Copy code
python app.py
By default, the app will be available at http://localhost:5000.

Web Interface
Start Listening: Click the "Start Listening" button to begin real-time speech recognition.
View Text and Translation: The recognized text and translated text will be displayed in real-time.
Hear Translation: The translated text will be played back as speech in the target language.
Tech Stack
Flask: Web framework used to create the web interface.
Google Speech Recognition API: Used for converting speech to text.
Transformers Library: Utilized for local NLP models for translation.
gTTS (Google Text-to-Speech): Converts translated text into speech.
PyAudio: Captures audio input from the user's microphone.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
Commit your changes and push to your fork.
Submit a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
