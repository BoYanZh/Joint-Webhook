from http import HTTPStatus
from webhook_elf.utils import webhook_push_task
from fastapi import APIRouter, Response, BackgroundTasks

from webhook_elf.schema import GiteaWebhook

router = APIRouter()


@router.post("/push", status_code=HTTPStatus.NO_CONTENT)
async def webhook_push(
    webhook: GiteaWebhook, background_tasks: BackgroundTasks
) -> Response:
    owner_name = webhook.repository.owner.username
    repo_name = webhook.repository.name
    latest_commit_id = webhook.commits[0].id
    background_tasks.add_task(
        webhook_push_task, owner_name, repo_name, latest_commit_id
    )
    return Response(status_code=HTTPStatus.NO_CONTENT.value)
