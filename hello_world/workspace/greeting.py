class Greeting:
    def __init__(self, language: str, text: str):
        self.language = language
        self.text = text

    def display(self):
        print(self.text)
