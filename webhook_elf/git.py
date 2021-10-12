import os
import pathlib
import shutil

from git import Repo
from git.exc import InvalidGitRepositoryError

from webhook_elf.config import settings


class Git:
    def __init__(self, repos_dir: str = settings.repos_dir):
        pathlib.Path(repos_dir).mkdir(parents=True, exist_ok=True)
        self.repos_dir = repos_dir

    def clone_repo(
        self, owner_name: str, repo_name: str, branch: str = "master"
    ) -> Repo:
        repo_dir = os.path.join(self.repos_dir, owner_name, repo_name)
        pathlib.Path(repo_dir).mkdir(parents=True, exist_ok=True)
        return Repo.clone_from(
            f"{settings.git_remote_url}/{owner_name}/{repo_name}.git",
            repo_dir,
            branch=branch,
        )

    def get_repo(self, owner_name: str, repo_name: str) -> Repo:
        repo_dir = os.path.join(self.repos_dir, owner_name, repo_name)
        if os.path.exists(repo_dir):
            try:
                return Repo(repo_dir)
            except InvalidGitRepositoryError:
                shutil.rmtree(repo_dir)
        return self.clone_repo(owner_name, repo_name)

    def repo_clean_and_checkout(
        self, owner_name: str, repo_name: str, checkout_dest: str
    ) -> str:
        repo_dir = os.path.join(self.repos_dir, owner_name, repo_name)
        repo = self.get_repo(owner_name, repo_name)
        repo.git.fetch("--tags", "--all", "-f")
        repo.git.reset("--hard", f"origin/master")
        repo.git.clean("-d", "-f", "-x")
        repo.git.checkout(checkout_dest)
        return repo_dir


if __name__ == "__main__":
    git = Git()
