from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "hello World"

@app.route('/items')
def items():
    items_list = ["Item 1", "Item 2", "Item 3"]
    return render_template('items.html')

@app.route("/tts")
def tts():
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

    return render_template('tts.html')

if __name__ == '__main__':
    app.run(debug=True)
