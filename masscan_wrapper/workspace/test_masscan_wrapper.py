import pytest
from masscan_wrapper.masscan_wrapper import MasscanWrapper, parse_output

def test_masscan_wrapper_init():
    wrapper = MasscanWrapper(rate=1000, exclusion_file="exclude.txt", hello_string="Hello", output_format="json")
    assert wrapper.rate == 1000
    assert wrapper.exclusion_file == "exclude.txt"
    assert wrapper.hello_string == "Hello"
    assert wrapper.output_format == "json"

def test_set_rate():
    wrapper = MasscanWrapper(rate=1000)
    wrapper.set_rate(2000)
    assert wrapper.rate == 2000

def test_set_exclusion_file():
    wrapper = MasscanWrapper(exclusion_file="exclude.txt")
    wrapper.set_exclusion_file("new_exclude.txt")
    assert wrapper.exclusion_file == "new_exclude.txt"

def test_set_hello_string():
    wrapper = MasscanWrapper(hello_string="Hello")
    wrapper.set_hello_string("New Hello")
    assert wrapper.hello_string == "New Hello"

def test_set_output_format():
    wrapper = MasscanWrapper(output_format="json")
    wrapper.set_output_format("xml")
    assert wrapper.output_format == "xml"

def test_run_scan(mocker):
    wrapper = MasscanWrapper(rate=1000, exclusion_file="exclude.txt", hello_string="Hello", output_format="json")
    mocker.patch("masscan_wrapper.masscan_wrapper.subprocess.run")
    wrapper.run_scan(target="127.0.0.1", ports="80,443")
    wrapper.subprocess.run.assert_called_once()

def test_parse_output():
    sample_output = '{"ip": "127.0.0.1", "ports": [{"port": 80, "proto": "tcp", "status": "open"}]}'
    parsed_output = parse_output(sample_output)
    assert parsed_output["ip"] == "127.0.0.1"
    assert parsed_output["ports"][0]["port"] == 80
    assert parsed_output["ports"][0]["proto"] == "tcp"
    assert parsed_output["ports"][0]["status"] == "open"
