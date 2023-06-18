import pytest
from greeting import Greeting

def test_greeting_constructor():
    greeting = Greeting("English", "Hello, World!")
    assert greeting.language == "English"
    assert greeting.text == "Hello, World!"

def test_greeting_display(capsys):
    greeting = Greeting("English", "Hello, World!")
    greeting.display()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
