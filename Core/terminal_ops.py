import subprocess

def run_command(command: str) -> bool:
    """Thực thi lệnh shell và trả về trạng thái thành công/thất bại."""
    try:
        # Chạy trên PowerShell
        subprocess.run(["powershell", "-Command", command], check=True)
        return True
    except subprocess.CalledProcessError:
        return False