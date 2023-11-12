from google.cloud import texttospeech
from google.oauth2 import service_account

class TextToSpeech:
    def __init__(self, output_path='output.mp3'):
        # hyper parameters are all default for now, future implementations will make
        # different voices and configurations possible
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
    def build_audio(self, text_input):
        synthesis_input = texttospeech.SynthesisInput(text=text_input)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )
        with open("output.mp3", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print("Audio content written to file 'output.mp3'")



def usage_example():
    tts = TextToSpeech()
    tts.build_audio('Hello, im Raul! How are you?')


if __name__ == '__main__':
    usage_example()