import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Import logic từ Core
from Core.ai_engine import chat_with_ai

console = Console()

def chat_command():
    """Mở chế độ trò chuyện liên tục với AI (Chat CLI)."""
    console.print(Panel.fit("[bold magenta]💬 Đang kết nối với OpenClaw... (Gõ 'exit' hoặc 'quit' để thoát)[/]", border_style="magenta"))
    
    messages = [
        {"role": "system", "content": "Bạn là OpenClaw Dev Assistant, một trợ lý lập trình chuyên nghiệp giúp developer giải quyết bug và tối ưu code."}
    ]
    
    while True:
        try:
            user_input = Prompt.ask("\n[bold green]Dev[/]")
            if user_input.lower() in ['exit', 'quit']:
                console.print("[dim]Tạm biệt! Hẹn gặp lại.[/]")
                break
            
            messages.append({"role": "user", "content": user_input})
            
            with console.status("[bold yellow]OpenClaw đang gõ...[/]", spinner="bouncingBar"):
                response = chat_with_ai(messages)
            
            console.print(f"\n[bold magenta]OpenClaw:[/] {response}")
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt: # Xử lý khi user bấm Ctrl+C
            console.print("\n[dim]Đã thoát phiên chat.[/]")
            break