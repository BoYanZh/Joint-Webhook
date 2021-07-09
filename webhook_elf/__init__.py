from fastapi import FastAPI, Request, status

from webhook_elf.api import router
from webhook_elf.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(router)
