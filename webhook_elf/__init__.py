from typing import Any

from fastapi import FastAPI, Request, status

from webhook_elf.config import settings
from webhook_elf.api import router

app = FastAPI(title=settings.app_name)

app.include_router(router)
