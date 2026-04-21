import os
from openai import OpenAI
from dotenv import load_dotenv

# Tải biến môi trường từ .env
load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_shell_command(user_query: str, os_name: str = "Windows") -> str:
    system_prompt = f"""Bạn là một trợ lý Terminal. OS: {os_name}.
    Chuyển đổi ngôn ngữ tự nhiên thành một dòng lệnh Terminal duy nhất.
    CHỈ trả về dòng lệnh, KHÔNG giải thích, KHÔNG dùng markdown ```bash."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def generate_commit_message(diff_content: str) -> str:
    system_prompt = """Bạn là một chuyên gia Git. Dựa vào đoạn git diff dưới đây, 
    hãy viết MỘT câu git commit message theo chuẩn Conventional Commits (vd: feat:, fix:, chore:, refactor:).
    CHỈ trả về đúng câu commit message, không giải thích gì thêm."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Git Diff:\n{diff_content[:3000]}"} # Cắt bớt nếu diff quá dài
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def chat_with_ai(messages: list) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Lỗi gọi API: {e}"