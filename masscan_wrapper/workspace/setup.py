from setuptools import setup, find_packages

setup(
    name="masscan-wrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
        ],
    },
    entry_points={},
)
