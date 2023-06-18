import pytest
from hello_world import HelloWorld

def test_hello_world_constructor():
    hello_world = HelloWorld()
    assert hello_world.language == "English"
    assert hello_world.text == "Hello, World!"

def test_hello_world_display(capsys):
    hello_world = HelloWorld()
    hello_world.display()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
