from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("template/index.html")
@app.route("/translate")
def translate_text():
    import requests

    url = "https://api.sarvam.ai/translate"

    payload = {
        "model": "mayura:v1",
        "mode": "formal",
        "speaker_gender": "Male",
        "target_language_code": "hi-IN",
        "source_language_code": "en-IN",
        "input": "My name is Ashutosh",
        "enable_preprocessing": True
    }
    headers = {
        "api-subscription-key": "82b84e3d-3b45-4f15-a98d-08f3b5a0d16d",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()

@app.route("/tts")
def text_to_speech():
    import requests

    url = "https://api.sarvam.ai/text-to-speech"

    payload = {
        "inputs": "My name is ashutosh",
        "target_language_code": "hi-IN",
        "speaker": "meera",
        "pitch": 0,
        "pace": 1.65,
        "loudness": 1.5,
        "speech_sample_rate": 8000,
        "enable_preprocessing": True,
        "model": "bulbul:v1"
    }
    headers = {
        "api-subscription-key": "82b84e3d-3b45-4f15-a98d-08f3b5a0d16d",
        "Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()
    

if __name__ == '__main__':
    app.run(debug=True)
