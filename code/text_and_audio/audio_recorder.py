import pyaudio
import threading
import wave
from time import sleep

class AudioRecorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = False

    def start(self):
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1,
                                      rate=44100, input=True, frames_per_buffer=1024)
        self.is_recording = True
        self.frames = []

        def record():
            while self.is_recording:
                data = self.stream.read(1024)
                self.frames.append(data)

        self.thread = threading.Thread(target=record)
        self.thread.start()

    def stop(self):
        self.is_recording = False


    def save(self, output_path: str):
        self.thread.join()

        # Save the recorded data as a WAV file
        with wave.open(output_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))

        # Close the stream
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        self.frames = []




def usage_example():
    recorder = AudioRecorder()
    recorder.start()  # Start recording
    sleep(3)
    recorder.stop()  # Stop recording
    recorder.save('opa.wav') # save


if __name__ == '__main__':
    usage_example()