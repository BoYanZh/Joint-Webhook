import subprocess
from typing import Tuple

from webhook_elf.config import settings
from webhook_elf.git import Git
from webhook_elf.gitea import Gitea


# TODO: Call elf here
def run_elf(repo_dir: str) -> Tuple[str, str]:
    subprocess.call([])
    return "", ""


git = Git()
gitea = Gitea(settings.gitea_access_token)


def webhook_push_task(owner_name: str, repo_name: str, latest_commit_id: str) -> None:
    reop_dir = git.repo_clean_and_checkout(owner_name, repo_name, latest_commit_id)
    title, body = run_elf(reop_dir)
    gitea.create_issue(owner_name, repo_name, title, body, False)
