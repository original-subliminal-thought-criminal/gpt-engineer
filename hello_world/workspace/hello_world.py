from greeting import Greeting

class HelloWorld(Greeting):
    def __init__(self):
        super().__init__("English", "Hello, World!")
