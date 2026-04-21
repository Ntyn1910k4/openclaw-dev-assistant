import typer
from rich.console import Console
from rich.panel import Panel

# Import logic từ Core
from Core.ai_engine import generate_shell_command
from Core.terminal_ops import run_command

console = Console()

def ask_command(query: str = typer.Argument(..., help="Mô tả lệnh bạn muốn thực hiện")):
    """Chuyển đổi ngôn ngữ tự nhiên thành lệnh Terminal."""
    with console.status(f"[bold green]🤖 OpenClaw đang phân tích:[/] '{query}'...", spinner="dots"):
        command = generate_shell_command(query, os_name="Windows PowerShell")
    
    if command.startswith("Error:"):
        console.print(f"[bold red]❌ {command}[/]")
        return

    console.print(Panel(f"[bold yellow]{command}[/]", title="Lệnh đề xuất", expand=False))

    if typer.confirm("Bạn có muốn chạy lệnh này ngay bây giờ không?"):
        if run_command(command):
             console.print("[bold green]✅ Đã chạy lệnh thành công![/]")
        else:
             console.print(f"[bold red]❌ Lỗi khi chạy lệnh. Hệ thống từ chối hoặc lệnh sai.[/]")
    else:
        console.print("[dim]Đã hủy thực thi lệnh.[/]")