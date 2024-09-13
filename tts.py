from google.cloud import texttospeech

def synthesize_speech(text):
    client = texttospeech.TextToSpeechClient.from_service_account_json('path/to/your/credentials.json')

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

synthesize_speech('Hello, world!')
