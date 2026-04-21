import git
from git.exc import InvalidGitRepositoryError

def get_staged_diff(repo_path: str = ".") -> str:
    """Lấy danh sách code đã được 'git add' (staged)."""
    try:
        repo = git.Repo(repo_path)
        return repo.git.diff('--cached')
    except InvalidGitRepositoryError:
        return "NOT_A_GIT_REPO"
    except Exception as e:
        return f"ERROR: {e}"

def commit_changes(message: str, repo_path: str = ".") -> bool:
    """Thực hiện lệnh commit với message tương ứng."""
    try:
        repo = git.Repo(repo_path)
        repo.index.commit(message)
        return True
    except Exception:
        return False