import pytest
from main import main

def test_main_execution(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
