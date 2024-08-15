from flask import Flask, render_template, jsonify
from gtts import gTTS
import os
import requests
import speech_recognition as sr
from dotenv import load_dotenv
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
TRANSLATION_SERVICE = os.getenv('TRANSLATION_SERVICE', 'local')
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
TARGET_LANGUAGE = 'de'  # German

# Initialize translation model for local setup
if TRANSLATION_SERVICE == 'local':
    tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return None

def translate_text(text):
    if TRANSLATION_SERVICE == 'deepl':
        url = "https://api.deepl.com/v2/translate"
        params = {
            "auth_key": DEEPL_API_KEY,
            "text": text,
            "target_lang": TARGET_LANGUAGE
        }
        response = requests.post(url, data=params)
        result = response.json()
        return result['translations'][0]['text']
    elif TRANSLATION_SERVICE == 'google':
        from google.cloud import translate_v2 as translate
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language=TARGET_LANGUAGE)
        return result['translatedText']
    elif TRANSLATION_SERVICE == 'local':
        inputs = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.get_lang_id(TARGET_LANGUAGE))
        return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

def speak_text(text):
    tts = gTTS(text=text, lang=TARGET_LANGUAGE)
    filepath = "static/output.mp3"
    tts.save(filepath)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    text = recognize_speech()
    if text:
        translated_text = translate_text(text)
        speak_text(translated_text)
        return jsonify({"text": text, "translated_text": translated_text})
    return jsonify({"error": "No speech detected"})

if __name__ == '__main__':
    app.run(debug=True)
