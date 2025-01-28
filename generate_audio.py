from google.cloud import texttospeech
import os

# Set up the Text-to-Speech client
client = texttospeech.TextToSpeechClient.from_service_account_json('C:/path/to/your/service-account-file.json')

# List of words and phrases to generate audio for
words = [
    "Finn",
    "Mom",
    "Want",
    "Dad",
    "Fun Sound 1",
    "Grandma",
    "Eat",
    "Declan",
    "Fun Sound 2",
    "Ashling",
    "Killian",
    "Don't Want",
    "Aunt",
    "Uncle",
    "Fun Sound 3",
    "Funny",
    "Fun Sound 4",
    "Watch",
    "Cuddle",
    "Baby",
    "Fun Sound 5",
    "Poop",
    "Sing",
    "Play",
    "Love",
    "Fun Sound 6",
    "Fun Sound 7"
]

# Create the audio directory if it doesn't exist
os.makedirs('audio', exist_ok=True)

# Generate audio files
for word in words:
    synthesis_input = texttospeech.SynthesisInput(text=word)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(f'audio/{word.replace(" ", "")}.mp3', 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "audio/{word.replace(" ", "")}.mp3"')
