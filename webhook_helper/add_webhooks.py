import focs_gitea

from webhook_elf.config import settings

configuration = focs_gitea.Configuration()
configuration.api_key["access_token"] = settings.gitea_access_token
configuration.host = settings.gitea_host
api_client = focs_gitea.ApiClient(configuration)
repository_api = focs_gitea.RepositoryApi(api_client)


def main() -> None:
    owner = "SilverFOCS-21"
    body = {
        "active": True,
        "branch_filter": "*",
        "config": {"content_type": "json", "url": "http://10.0.3.179:8000/push"},
        "events": ["push"],
        "type": "gitea",
    }
    for i in range(1, 14):
        repo = f"p1team{i}"
        create_res = repository_api.repo_create_hook(owner, repo, body=body)
        repository_api.repo_test_hook(owner, repo, create_res.id)


if __name__ == "__main__":
    main()
