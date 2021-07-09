import focs_gitea

from webhook_elf.config import settings


class Gitea:
    def __init__(self, access_token: str = settings.gitea_access_token):
        configuration = focs_gitea.Configuration()
        configuration.api_key["access_token"] = access_token
        configuration.host = settings.gitea_host
        self.api_client = focs_gitea.ApiClient(configuration)
        self.admin_api = focs_gitea.AdminApi(self.api_client)
        self.miscellaneous_api = focs_gitea.MiscellaneousApi(self.api_client)
        self.organization_api = focs_gitea.OrganizationApi(self.api_client)
        self.issue_api = focs_gitea.IssueApi(self.api_client)
        self.repository_api = focs_gitea.RepositoryApi(self.api_client)
        self.settings_api = focs_gitea.SettingsApi(self.api_client)
        self.user_api = focs_gitea.UserApi(self.api_client)

    def create_issue(
        self,
        owner_name: str,
        repo_name: str,
        title: str,
        body: str,
        assign_every_collaborators: bool = True,
    ) -> None:
        assignees = []
        if assign_every_collaborators:
            assignees = [
                item.username
                for item in self.repository_api.repo_list_collaborators(
                    owner_name, repo_name
                )
            ]
        self.issue_api.issue_create_issue(
            owner_name,
            repo_name,
            body={"title": title, "body": body, "assignees": assignees},
        )


if __name__ == "__main__":
    gitea = Gitea()
