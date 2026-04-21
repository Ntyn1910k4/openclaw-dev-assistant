from setuptools import setup, find_packages

setup(
    name="openclaw",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "rich",
        "openai",
        "gitpython",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "claw=main:app", # Lệnh 'claw' sẽ gọi app Typer trong main.py
        ],
    },
)