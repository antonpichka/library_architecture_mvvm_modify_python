from setuptools import setup

setup(
    name="example",
    version="0.0.1",
    install_requires=[
        "library-architecture-mvvm-modify-python",
        "requests==2.32.3"
    ],
    entry_points={
        "console_scripts": [
            "program = main:main"
        ]
    }
)