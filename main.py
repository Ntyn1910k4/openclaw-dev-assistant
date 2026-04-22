import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import typer
from Commands.chat import chat_command

app = typer.Typer(help="OpenClaw Dev Assistant CLI - Bản V2")

# THÊM 3 DÒNG NÀY VÀO ĐỂ ÉP GIỮ CẤU TRÚC LỆNH
@app.callback()
def callback():
    pass

@app.command(name="chat", help="Mở chế độ trò chuyện với AI")
def chat_cmd():
    chat_command()

if __name__ == "__main__":
    app()