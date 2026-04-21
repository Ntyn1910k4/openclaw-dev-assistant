import typer

# Import các hàm lệnh từ thư mục Commands
from Commands.ask import ask_command
from Commands.git import git_assist
from Commands.chat import chat_command

# Khởi tạo ứng dụng chính của OpenClaw
app = typer.Typer(help="OpenClaw Dev Assistant - Trợ lý AI cho Terminal & Git")

# Đăng ký (gắn) các lệnh vào ứng dụng
app.command("ask")(ask_command)
app.command("git-assist")(git_assist)
app.command("chat")(chat_command)

if __name__ == "__main__":
    # Điểm bắt đầu của chương trình
    app()