from playsound import playsound


# this is a temporary implementation
# will be changed in the future in order to
# control stopping of the audio play

def play_audio(file_path):
    playsound(file_path)

def example_usage():
    play_audio('../gpt.mp3')

if __name__ == '__main__':
    example_usage()
