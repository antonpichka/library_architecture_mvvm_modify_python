from setuptools import setup

setup(
    name="example",
    version="0.0.1",
    install_requires=[
        "library_architecture_mvvm_modify_python",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "program = main:main"
        ]
    }
)