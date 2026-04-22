from setuptools import setup, find_packages

setup(
    name="openclaw",
    version="0.1.0",
    py_modules=['main'],
    packages=find_packages(),
    install_requires=[
        "typer", 
        "rich", 
        "mistralai", 
        "python-dotenv", 
        "gitpython"
    ],
    entry_points={
        "console_scripts": [
            "claw=main:app",
        ],
    },
)