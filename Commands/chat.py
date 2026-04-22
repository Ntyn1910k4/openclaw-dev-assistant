from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from Core.ai_engine import chat_with_ai

console = Console()

def chat_command():
    console.print(Panel.fit(
        "[bold magenta]💬 OpenClaw V2 đã sẵn sàng! (Gõ 'exit' để thoát)[/]", 
        border_style="magenta"
    ))
    
    # Lời chào ban đầu (System Prompt)
    messages = [
        {"role": "system", "content": "Bạn là trợ lý ảo OpenClaw dành cho lập trình viên. Hãy trả lời ngắn gọn, súc tích và chuyên nghiệp."}
    ]
    
    while True:
        try:
            user_input = Prompt.ask("\n[bold green]Dev[/]")
            if user_input.lower() in ['exit', 'quit']:
                console.print("[dim]Tạm biệt! Hẹn gặp lại.[/]")
                break
            
            messages.append({"role": "user", "content": user_input})
            
            with console.status("[bold yellow]AI đang suy nghĩ...[/]", spinner="bouncingBar"):
                response = chat_with_ai(messages)
            
            console.print(f"\n[bold magenta]OpenClaw:[/] {response}")
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            console.print("\n[dim]Đã thoát phiên chat.[/]")
            break