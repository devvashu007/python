from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to the Flask App</h1>
    <p>Use the following endpoints to test:</p>
    <ul>
        <li><a href="/translate">Translate Text</a></li>
        <li><a href="/tts">Text-to-Speech</a></li>
    </ul>
</body>
</html>
'''
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

    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text-to-Speech Audio Playback</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        .container {
            text-align: center;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Text-to-Speech Audio Playback</h1>
        <audio id="audio-player" controls>
            Your browser does not support the audio element.
        </audio>
        <br>
        <button onclick="playAudio()">Play Audio</button>
    </div>

    <script>
        function playAudio() {
            const audioPlayer = document.getElementById('audio-player');
            audioPlayer.src = '/get-audio';
            audioPlayer.play();
        }
    </script>
</body>
</html>
'''
    

if __name__ == '__main__':
    app.run(debug=True)
