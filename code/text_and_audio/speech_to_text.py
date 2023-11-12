from google.cloud import speech
import io

def speech_to_text(
    config: speech.RecognitionConfig,
    audio: speech.RecognitionAudio,
) -> speech.RecognizeResponse:
    client = speech.SpeechClient()

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)

    return response

def print_response(response: speech.RecognizeResponse):
    for result in response.results:
        print_result(result)

def print_result(result: speech.SpeechRecognitionResult):
    best_alternative = result.alternatives[0]
    print("-" * 80)
    print(f"language_code: {result.language_code}")
    print(f"transcript:    {best_alternative.transcript}")
    print(f"confidence:    {best_alternative.confidence:.0%}")

# Load the local MP3 file
file_name = 'output.mp3'  # Path to your MP3 file
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    language_code="en-US",  # Adjust the language code if necessary
    sample_rate_hertz=16000  # Set this to the sample rate of your MP3 file, if known
)
audio = speech.RecognitionAudio(
    content=content,
)

response = speech_to_text(config, audio)
print_response(response)
