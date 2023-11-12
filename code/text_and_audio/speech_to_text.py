from google.cloud import speech
import io



def load_audio_file(file_name='input.mp3'):
    with io.open(file_name, "rb") as audio_file:
        return audio_file.read()

class SpeechToText:
    def __init__(self):
        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            language_code="en-US",  # Adjust the language code if necessary
            sample_rate_hertz=16000  # Set this to the sample rate of your MP3 file, if known
        )

    def get_best_transcription(self, transcription: speech.SpeechRecognitionResult):   
        return transcription.results[0].alternatives[0].transcript   

    def get_best_transcription_confidence(self, transcription: speech.SpeechRecognitionResult):
        return transcription.results[0].alternatives[0].confidence
    
    def get_transcription_lc(self, transcription: speech.SpeechRecognitionResult):
        return transcription.results[0].language_code

    def transcribe(self, input_path='input.mp3'):
        content = load_audio_file(input_path)
        audio = speech.RecognitionAudio(
            content=content,
        )
        return self.client.recognize(config=self.config, audio=audio)
    


def usage_example():
    stt = SpeechToText()
    trsc = stt.transcribe('output.mp3')
    print(stt.get_best_transcription(trsc))
    print(stt.get_best_transcription_confidence(trsc))
    print(stt.get_transcription_lc(trsc))
    


if __name__ == '__main__':
    usage_example()
