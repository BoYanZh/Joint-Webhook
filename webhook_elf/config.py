from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Webhook Elf"

    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = False

    # gitea
    gitea_host: str = "https://focs.ji.sjtu.edu.cn/git/api/v1"
    gitea_access_token: str = ""
    gitea_issue_title: str = "{time} - Elf report"

    # git
    git_remote_url: str = "ssh://git@focs.ji.sjtu.edu.cn:2222"
    repos_dir: str = "./repos"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
