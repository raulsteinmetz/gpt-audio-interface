from openai import OpenAI

class GPTPrompter:
    def __init__(self):
        self.client = OpenAI(
          api_key='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'
        )
        self.model = 'gpt-3.5-turbo' # for now, plan to change for gpt 4 later

    def prompt_gpt(self, prompt):
        return self.client.chat.completions.create(
            model = self.model,
            messages = prompt
        )
    
    def get_best_answer(self, answer):
        return answer.choices[0].message.content
  

def usage_example():
    prompter = GPTPrompter()

    prompt = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]

    print(prompter.get_best_answer(prompter.prompt_gpt(prompt)))


if __name__ == '__main__':
    usage_example()


