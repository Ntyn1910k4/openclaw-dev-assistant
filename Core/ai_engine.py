import os
from pathlib import Path
from dotenv import load_dotenv

# ĐÂY LÀ DÒNG IMPORT CHUẨN CỦA MISTRAL BẢN 2.4.1
from mistralai.client import Mistral

# Ép đọc file .env ở thư mục gốc (OpenClaw Dew)
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path, override=True)

# Khởi tạo Mistral Client
api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

def chat_with_ai(messages: list) -> str:
    if not os.getenv("MISTRAL_API_KEY"):
        return "Lỗi: Không tìm thấy MISTRAL_API_KEY trong file .env. Hãy kiểm tra lại!"

    try:
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Lỗi gọi AI Mistral: {e}"