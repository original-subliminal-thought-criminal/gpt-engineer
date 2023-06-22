import subprocess
from typing import Dict, Any


class MasscanWrapper:
    def __init__(self, rate: int, exclusion_file: str, hello_string: str, output_format: str):
        self.rate = rate
        self.exclusion_file = exclusion_file
        self.hello_string = hello_string
        self.output_format = output_format

    def set_rate(self, rate: int):
        self.rate = rate

    def set_exclusion_file(self, exclusion_file: str):
        self.exclusion_file = exclusion_file

    def set_hello_string(self, hello_string: str):
        self.hello_string = hello_string

    def set_output_format(self, output_format: str):
        self.output_format = output_format

    def run_scan(self, target: str, ports: str) -> Dict[str, Any]:
        cmd = [
            "masscan",
            "-p", ports,
            "--rate", str(self.rate),
            "--excludefile", self.exclusion_file,
            "--hello-string", self.hello_string,
            "--output-format", self.output_format,
            target,
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return parse_output(result.stdout)


def parse_output(output: str) -> Dict[str, Any]:
    if output_format == "json":
        return json.loads(output)
    elif output_format == "xml":
        # Implement XML parsing here
        pass
    else:
        raise ValueError("Unsupported output format")
