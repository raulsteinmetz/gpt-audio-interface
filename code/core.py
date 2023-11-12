from gpt_prompts.gpt4 import GPTPrompter
from text_and_audio.audio_recorder import AudioRecorder
from text_and_audio.speech_to_text import SpeechToText
from text_and_audio.text_to_speech import TextToSpeech
from text_and_audio.audio_player import play_audio
from time import sleep


class ConversationCore:
    def __init__(self):
        self.mem = []
        self.tts = TextToSpeech()
        self.stt = SpeechToText()
        self.gpt = GPTPrompter()

    def feed_mem(self, message):
        self.mem.append(message)

    def setup(self):
        self.feed_mem({'role': 'system', 'content': 'You are an English Teacher, \
                        answer questions with simple lenguage, \
                        be friendly'}) # for now, more complex and advanced options later
        self.feed_mem({'role': 'system', 'content': 'start the conversation saying \
                        your name, which is GPT Pal, and explaining \
                        that you are a assistent desinged to answer \
                        questions and help in lenguage learning'})
        

    def main_loop(self):
        done = False

        # GPT INTRODUCTION
        best_answer = self.gpt.get_best_answer(
            self.gpt.prompt_gpt(self.mem)
        ) # gets gpt best answer based on previous conversaton

        self.feed_mem({'role': 'assistant', 'content': best_answer})
        
        # TEXT TO SPEECH
        self.tts.build_audio(best_answer, 'gpt.mp3') # getting audio from gpt response

        # PLAY GPT AUDIO
        play_audio('gpt.mp3')



        while not done:
            audio_recorder = AudioRecorder()
            # USER AUDIO RECORDING
            print('\n\nUser can now speek\n\n')
            audio_recorder.start()
            sleep(10) # for now, 10 seconds for user to speak
            audio_recorder.stop()
            print('Stopped Recording\n\n')
            audio_recorder.save('user.wav')
            

            # SPEECH TO TEXT
            user_message = self.stt.get_best_transcription(self.stt.transcribe('user.wav'))
            self.feed_mem({'role': 'user', 'content': user_message})

            # PROMPTING
            best_answer = self.gpt.get_best_answer(
                self.gpt.prompt_gpt(self.mem)
            ) # gets gpt best answer based on previous conversaton
            self.feed_mem({'role': 'assistant', 'content': best_answer})

            # TEXT TO SPEECH
            self.tts.build_audio(best_answer, 'gpt.mp3') # getting audio from gpt response

            # PLAY GPT AUDIO
            play_audio('gpt.mp3')



    def start_conversation(self):
        self.setup()
        self.main_loop()




def main():
    teacher = ConversationCore()
    teacher.start_conversation()


if __name__ == '__main__':
    main()


