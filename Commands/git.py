import typer
from rich.console import Console
from rich.panel import Panel

# Import logic từ Core
from Core.git_tools import get_staged_diff, commit_changes
from Core.ai_engine import generate_commit_message

console = Console()

def git_assist(action: str = typer.Argument("commit", help="Hành động Git (mặc định: commit)")):
    """Trợ lý Git (Tự động đọc diff và viết Commit Message)."""
    if action == "commit":
        with console.status("[bold blue]🐙 Đang đọc file đã staged (git diff --cached)...[/]"):
            diff = get_staged_diff()
            
        if diff == "NOT_A_GIT_REPO":
            console.print("[bold red]❌ Thư mục hiện tại không phải là Git Repository![/]")
            return
        elif not diff or diff.startswith("ERROR"):
            console.print("[yellow]⚠️ Không có file nào được 'git add' hoặc không có thay đổi nào.[/]")
            return

        with console.status("[bold blue]🧠 AI đang viết commit message...[/]"):
            commit_msg = generate_commit_message(diff)

        console.print(Panel(f"[bold cyan]{commit_msg}[/]", title="Commit Message Đề Xuất", expand=False))
        
        if typer.confirm("Bạn có muốn commit với tin nhắn này không?"):
            if commit_changes(commit_msg):
                console.print("[bold green]✅ Commit thành công![/]")
            else:
                console.print("[bold red]❌ Có lỗi xảy ra khi commit![/]")
        else:
            console.print("[dim]Đã hủy commit.[/]")
    else:
        console.print(f"[yellow]Tính năng '[bold]{action}[/]' đang được team phát triển![/]")