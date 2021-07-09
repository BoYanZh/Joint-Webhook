import subprocess
import sys
from datetime import datetime
from typing import Tuple

from webhook_elf.config import settings
from webhook_elf.git import Git
from webhook_elf.gitea import Gitea

git = Git()
gitea = Gitea(settings.gitea_access_token)


def run_elf(repo_dir: str) -> Tuple[str, str]:
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    title = settings.gitea_issue_title.format(time=time)
    # TODO: Call elf here
    command = ["ls", repo_dir]
    body = subprocess.check_output(command).decode(sys.stdout.encoding).strip()
    return title, body


def webhook_push_task(owner_name: str, repo_name: str, latest_commit_id: str) -> None:
    reop_dir = git.repo_clean_and_checkout(owner_name, repo_name, latest_commit_id)
    title, body = run_elf(reop_dir)
    gitea.create_issue(owner_name, repo_name, title, body, False)
